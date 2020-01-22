import subprocess
import logging
import rq
from redis import Redis
from rq.job import Job
import time

import settings

redis = Redis()

logger = logging.getLogger(__name__)

def initLogger():

    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
    file_handler = logging.FileHandler(settings.logFilePath 
                                        +__name__ 
                                        + '_' 
                                        + str(int(time.time())) 
                                        + '.log'
                                        )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)







def checkJob(jobID):
    if settings.debugMode:
        logging.info("check job by id : %s",jobID)

    job = Job.fetch(jobID, connection=redis)
    return job.meta[settings.jobMetaOuput]


def do_render_anim(jobID,startFrame,endFrame):

    # better logging info  TODO
    if settings.debugMode:
        logging.info("request render anim with job id: %s ",jobID)

    try:
        proc = subprocess.Popen([settings.blenderExcPath,
                                "-b",
                                settings.testBlenderFilePath,
                                "-o",
                                settings.testOutputPath,
                                "-s",
                                str(startFrame),
                                "-e",
                                str(endFrame),
                                "-a"], 
                bufsize=1,
                stdout=subprocess.PIPE, 
                stderr=subprocess.STDOUT,
                timeout=settings.subProcTimeout,
                universal_newlines=True)

        while proc.poll() is None:
            line = proc.stdout.readline()
            if line:
                # Process output here
                job = Job.fetch(jobID, connection=redis)
                job.meta[settings.jobMetaOuput] = line
                job.save_meta()

    except Exception as e:
        logging.error(e)

    except subprocess.TimeoutException as e:
        logging.error('Process was killed by timeout.')

    except subprocess.CalledProcessError as e:
        logging.error(e)


    finally:
        if proc.poll() is None:
            proc.kill()
            stdout, stderr = proc.communicate()
            logging.error(stderr)



def do_render_frame(jobID,frameNr):

    # better logging info  TODO like file name , output path, frame
    if settings.debugMode:
        logging.info("request render anim with job id: %s ",jobID)


    try:
        proc = subprocess.Popen([settings.blenderExcPath,
                                "-b",
                                settings.testBlenderFilePath,
                                "-o",
                                settings.testOutputPath,
                                "-f",
                                str(frameNr)], 
                bufsize=1,
                stdout=subprocess.PIPE, 
                stderr=subprocess.STDOUT,
                universal_newlines=True)

        while proc.poll() is None:
            line = proc.stdout.readline()
            if line:
                # Process output here
                job = Job.fetch(jobID, connection=redis)
                job.meta[settings.jobMetaOuput] = line
                job.save_meta()


    except Exception as e:
        logging.error(e)

    except subprocess.TimeoutException as e:
        logging.error('Process was killed by timeout.')

    except subprocess.CalledProcessError as e:
        logging.error(e)


    finally:
        if proc.poll() is None:
            proc.kill()
            stdout, stderr = proc.communicate()
            logging.error(stderr)



initLogger()

# ===========================================================
def updateJobMetaTs(jobID):
    job = Job.fetch(jobID, connection=redis)
    job.meta['ts'] = time.time()
    # print(job.meta['ts'])




