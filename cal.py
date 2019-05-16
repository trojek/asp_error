from datetime import datetime, timedelta
from aps import scheduler
import random




def start_watch_calendar(calendar_id, user_id):
    print(calendar_id, user_id)
    renew_time = datetime.now() + timedelta(minutes=1)
    cal_id = random.randint(0, 100)
    u_id = random.randint(0, 100)

    scheduler.add_job(start_watch_calendar, 'date', run_date=renew_time, args=[
        cal_id, u_id], misfire_grace_time=60 * 60 * 24)
