from flask import Flask
from aps import scheduler
from cal import start_watch_calendar

app = Flask(__name__)

if __name__ == '__main__':
    # app.run()
    scheduler.start()
    scheduler.print_jobs()
    start_watch_calendar(100, 100)
    app.run()
    
