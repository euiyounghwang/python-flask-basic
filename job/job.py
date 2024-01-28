
from apscheduler.schedulers.background import BackgroundScheduler
import time
from threading import Thread


# Declaration of the task as a function.
def print_date_time():
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))

def thread_background():
    while True:
        try:
            print('--thread_background--')
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
    
  