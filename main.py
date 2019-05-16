from flask import Flask
from cal import start_watch_calendar

app = Flask(__name__)
start_watch_calendar(100, 100)

if __name__ == '__main__':
    # app.run()
    app.run()
    
