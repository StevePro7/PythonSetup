How to Route Celery Tasks
07-Sep-2024

https://medium.com/@johnidouglasmarangon/how-to-route-celery-tasks-401c13b157df

Celery
Python distributed task framework

Tasks
asynchronous functions run outside main program


Producers
sends tasks to the message broker
e.g. API send tasks to broker when user makes request


Broker
intermediary btwn producer + consumer
e.g. brokers
Redis
RabbitMS
Amazon SQS      Simple Queue Service
responsible for receiving messages from producers and
forwarding them to consumers


Consumers
workers that execute the tasks recieved from the message broker
executors of tasks - can be on same or different machines to producer


Scale
task processing:

Horizontally
add more workers as needed


TUTORIAL
pip install 'celery[redis]' fastapi uvicorn
pip install --upgrade pip

docker run -p 6379:6379 redis


NB:
want to try ruff also

ruff check .
ruff format .

ruff check --select I --fix
# SORTS imports
