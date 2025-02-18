How to Route Celery Tasks
18-Feb-2025

https://medium.com/@johnidouglasmarangon/how-to-route-celery-tasks-401c13b157df


GPT
python celery broker how to debug consumer


1. Enable Celery Logging
celery -A myapp worker --loglevel=DEBUG


2. Use Flower for Real-Time Monitoring
pip install flower

celery -A myapp flower
http://localhost:5555


3. Debugging Task Execution with Celery
from celery import Celery
import logging

app = Celery('myapp', broker='your_broker_url')

@app.task(bind=True)
def my_task(self, *args, **kwargs):
    logging.debug("Task started")
	

Use a Debugger (e.g., pdb):
import pdb
from celery import Celery

app = Celery('myapp', broker='your_broker_url')

@app.task
def my_task():
    pdb.set_trace()  # This will pause the execution here
	
	
4. Check Broker Configuration
Redis
redis-server

check redis running if responds with pong
redis-cli ping

RabbitMQ
rabbitmq-server


5. Monitor the Queue
celery -A myapp status


6. Check Worker Health
celery -A myapp status


7. Check for Errors in the Broker
RabbitMQ
log files
/var/log/rabbitmq/


8. Isolate Specific Tasks

from myapp.tasks import my_task
my_task.apply_async(args=[...])


9. Use Celery’s -Q Flag to Specify Queue
celery -A myapp worker -Q your_queue_name --loglevel=DEBUG
