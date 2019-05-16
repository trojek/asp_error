from pymongo import MongoClient
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
import random
from flask import Flask

def scheduler_initialize():
    client = MongoClient(
        "mongodb+srv://apscheduler:GiVExzzFov38gxrQ@cluster0-s0oj3.mongodb.net/test?retryWrites=true")

    apscheduler = BackgroundScheduler()
    apscheduler.add_jobstore(
        'mongodb', collection='watch_calendars', client=client)
    apscheduler.start()
    apscheduler.print_jobs()
    # scheduler.remove_all_jobs()
    # log.info('Advanced Python scheduler (mongo job store) initialized...')
    return apscheduler


def start_watch_calendar(calendar_id, user_id):
    print(calendar_id, user_id)
    renew_time = datetime.now() + timedelta(minutes=1)
    cal_id = random.randint(0, 100)
    u_id = random.randint(0, 100)

    scheduler.add_job(start_watch_calendar, 'date', run_date=renew_time, args=[
        cal_id, u_id], misfire_grace_time=60 * 60 * 24)

scheduler = scheduler_initialize()
app = Flask(__name__)
start_watch_calendar(100, 100)

if __name__ == '__main__':
    # app.run()
    app.run()
    
