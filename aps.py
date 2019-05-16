from apscheduler.schedulers.background import BackgroundScheduler
from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://apscheduler:GiVExzzFov38gxrQ@cluster0-s0oj3.mongodb.net/test?retryWrites=true")
scheduler = BackgroundScheduler()
scheduler.add_jobstore(
    'mongodb', collection='watch_calendars', client=client)
