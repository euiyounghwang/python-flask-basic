
from apscheduler.schedulers.background import BackgroundScheduler
import time
import threading
import asyncio


# Declaration of the task as a function.
def print_date_time():
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))


def create_jobs():
    # Create the background scheduler
    scheduler = BackgroundScheduler()
    # Create the job
    scheduler.add_job(func=print_date_time, trigger="interval", seconds=10)
    # Start the scheduler
    scheduler.start()
    
  