
from apscheduler.schedulers.background import BackgroundScheduler
import time
from threading import Thread
from api import logger
from .kafka_job import consumer_kafka

# Declaration of the task as a function.
def print_date_time():
    logger.info(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))


def thread_background():
    while True:
        try:
            logger.info('--thread_background--')
            consumer_kafka()
        except Empty:
            pass
        time.sleep(5)  # TODO poll other things



def create_jobs():
    # Create the background scheduler
    scheduler = BackgroundScheduler()
    # Create the job
    scheduler.add_job(func=print_date_time, trigger="interval", seconds=10)
    # Start the scheduler
    scheduler.start()
    
    # Create thread as background
    Thread(target=thread_background, daemon=True).start()
    
  