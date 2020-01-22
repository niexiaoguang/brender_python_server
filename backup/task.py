import requests
import subprocess
import logging
import rq
from redis import Redis
from rq.job import Job
import time

redis = Redis()

def count_words_at_url(url):
    resp = requests.get(url)
    return len(resp.text.split())


def render():
    do_render()


def updateJobMeta(jobID):
    job = Job.fetch(jobID, connection=redis)
    job.meta['ts'] = time.time()
    print(job.meta['ts'])
    print(job.meta['output'])



blenderExcPath = "/home/pata/blender/blender-2.81a-linux-glibc217-x86_64/blender"
blenderFilePath = "/home/pata/data/test_cycles_cpu.blend"
outputPath = "/home/pata/nginx/html/rendered/frame_###"
frameNr = 17

jobID = 'myJobId'

def do_render():


    proc = subprocess.Popen([blenderExcPath,"-b",blenderFilePath,"-o",outputPath,"-f",str(frameNr)], 
            bufsize=1,
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT,
            universal_newlines=True)

    while proc.poll() is None:
        line = proc.stdout.readline()
        if line:
            # Process output here
            job = Job.fetch(jobID, connection=redis)
            job.meta['output'] = line
            job.save_meta()
