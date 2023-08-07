from dotenv import load_dotenv

from notification_system.models import session
from notification_system.models import worker_sensor


from datetime import datetime

if __name__ == '__main__':
    session
    table = worker_sensor.insert().values(sensor_id=2, worker_id=9, alert_time=datetime.now())
    session.begin()
    session.execute(table)
    session.commit()
    