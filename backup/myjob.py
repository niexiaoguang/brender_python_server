from redis import Redis
from rq.job import Job
from rq import Queue


import time
import subprocess

from worker import conn

redis_conn = Redis()
redis_conn = conn

q = Queue(connection=redis_conn)  # no args implies the default queue

jobID = 'myJob'

blenderExcPath = "/home/pata/blender/blender-2.81a-linux-glibc217-x86_64/blender"
blenderFilePath = "/home/pata/data/test_cycles_cpu.blend"
outputPath = "/home/pata/nginx/html/rendered/frame_###"
frameNr = 8
def do_render():
    p = subprocess.run([
            blenderExcPath,
            "-b",
            blenderFilePath,
            "-o",
            outputPath,
            "-f",
            str(frameNr)],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,#output error combine into stdout
        check=True)

    return p # output std and err info via PIPE to caller
    # print(res.stdout)
    # print(res.returncode)  

    # print(res.stderr) # check=True will output trackback info about error


def newJob():

    # stdout,stderr = p.communicate()
    # pstdout,pstderr = p.communicate()
    # job.meta['output'] = ''
    # job.save()

    # job = Job.create(do_render,timeout='1h',id=jobID)
    # q.enqueue_job(job)

    # while True:
    #     time.sleep(2)
    #     print(job.get_status())

    p = do_render()
    while True:
        time.sleep(2)
        print("std" + p.stdout)



if __name__ == '__main__':
    newJob()
