from rq import Queue
from worker import conn
import time

from task import count_words_at_url
# from task import oscmd
from task import render
from task import updateJobMeta
q = Queue(connection=conn)

jobID = 'myJobId'
# result = q.enqueue(count_words_at_url, 'http://www.heroku.com',job_id=jobID)
# result = q.enqueue(oscmd)

job = q.enqueue(render,job_id=jobID)
job.meta['output'] = 'init'
job.save_meta()


while True:
	time.sleep(2)
	updateJobMeta(jobID)