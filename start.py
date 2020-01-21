from rq import Queue
from worker import conn

from task import count_words_at_url
from task import oscmd

q = Queue(connection=conn)

# result = q.enqueue(count_words_at_url, 'http://www.heroku.com')
result = q.enqueue(oscmd)

print(result)