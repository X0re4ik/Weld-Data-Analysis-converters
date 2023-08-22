import sqlalchemy as db 

from datetime import datetime
from sqlalchemy.orm import create_session, relationship
from sqlalchemy.ext.declarative import declarative_base

from notification_system.configs import DB_URI

_engine = db.create_engine(DB_URI)
_Base = declarative_base(bind=_engine)

session = create_session(bind=_engine)


class Sensor(_Base):
    __table__ = db.Table('sensor', _Base.metadata, autoload=True)
    
    def as_dict(self, deep=True):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Worker(_Base):
    __table__ = db.Table('worker', _Base.metadata, autoload=True)
    
    def as_dict(self, deep=True):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Master(_Base):
    __table__ = db.Table('master', _Base.metadata, autoload=True)
    
    def as_dict(self, deep=True):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
class Welder(_Base):
    __table__ = db.Table('welder', _Base.metadata, autoload=True)
    
    def as_dict(self, deep=True):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    

class WeldingWireDiameter(_Base):
    __table__ = db.Table('welding_wire_diameter', _Base.metadata, autoload=True)
    
    def as_dict(self, deep=True):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class WeldingGas(_Base):
    __table__ = db.Table('welding_gas', _Base.metadata, autoload=True)
    
    def as_dict(self, deep=True):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
        
class WeldMetal(_Base):
    __table__ = db.Table('weld_metal', _Base.metadata, autoload=True)
    
    def as_dict(self, deep=True):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
        
class Measurement(_Base):
    __table__ = db.Table('measurement', _Base.metadata, autoload=True)
    
    def as_dict(self, deep=True):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    
class DailyReport(_Base):
    __table__ = db.Table('daily_report', _Base.metadata, autoload=True)
    
    def as_dict(self, deep=True):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    

# class NotificationDate(_Base):
#     __tablename__ = 'notification_date'
    
#     id = db.Column(db.Integer, primary_key=True)
    
#     worker_id = db.Column(db.Integer, db.ForeignKey(Worker.id), nullable=False, unique=True)
#     alert_time = db.Column(db.Time, nullable=False)
#     day_of_week = db.Column(db.Integer, nullable=False)
    
    

# class SensorFileReports(_Base):
#     __tablename__ = 'sensor_file_reports'
    
#     id = db.Column(db.Integer, primary_key=True)
    
#     sensor_id = db.Column(db.Integer, db.ForeignKey(Sensor.id), nullable=False)
#     date = db.Column(db.Date, default=datetime.now(), nullable=False)
#     path_to_pdf_file = db.Column(db.Text, nullable=False)


# worker_sensor = db.Table('worker_sensor',
#                     _Base.metadata,
#                     db.Column('worker_id', db.Integer, db.ForeignKey('public.worker.id'), nullable=False),
#                     db.Column('sensor_id', db.Integer, db.ForeignKey('public.sensor.id'), nullable=False))

_Base.metadata.create_all(bind=_engine)