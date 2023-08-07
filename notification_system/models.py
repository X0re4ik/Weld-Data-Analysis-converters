from sqlalchemy import *
from sqlalchemy.orm import create_session
from sqlalchemy.ext.declarative import declarative_base


from notification_system.configs import DB_URI

_engine = create_engine(DB_URI)
metadata = MetaData(bind=_engine)
session = create_session(bind=_engine)

Base = declarative_base()

class Sensor(Base):
    __table__ = Table('sensor', metadata, autoload=True)

class Worker(Base):
    __table__ = Table('worker', metadata, autoload=True)

class Master(Base):
    __table__ = Table('master', metadata, autoload=True)
    
class Welder(Base):
    __table__ = Table('welder', metadata, autoload=True)
    
class Admin(Base):
    __table__ = Table('admin', metadata, autoload=True)

class WeldingWireDiameter(Base):
    __table__ = Table('welding_wire_diameter', metadata, autoload=True)
        
class WeldMetal(Base):
    __table__ = Table('weld_metal', metadata, autoload=True)
        
class Measurement(Base):
    __table__ = Table('measurement', metadata, autoload=True)
    
    
class DailyReport(Base):
    __table__ = Table('daily_report', metadata, autoload=True)
    


worker_sensor = Table('worker_sensor',
                    metadata,
                    Column('worker_id', Integer, ForeignKey('worker.id'), nullable=False),
                    Column('sensor_id', Integer, ForeignKey('sensor.id'), nullable=False),
                    Column('alert_time', Time, nullable=False),
                    Column('day_of_week', Integer, nullable=False)
                    )

metadata.create_all(_engine)