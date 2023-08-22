from datetime import date
from pathlib import Path
from abc import ABC, abstractmethod

from notification_system.models import session

from notification_system.models import Sensor, DailyReport, Measurement, WeldingGas, WeldingWireDiameter, WeldMetal
from sqlalchemy import and_, func


from typing import List

class WeldingProcessParameters:
    def __init__(self, wire_diameter: float, metal_density: float, metal_type: str, gas_type: str) -> None:
        self.wire_diameter: float   = wire_diameter
        self.metal_density: float   = metal_density
        self.metal_type:    str     = metal_type
        self.gas_type:      str     = gas_type
    

class DataBaseDataStore:
    
    def __init__(self, mac_address: str, date: date, session_) -> None:
        self.session = session_
        self._date = date
        self._mac_address = mac_address

        self._sensor = self.session.query(Sensor).filter(Sensor.mac_address==mac_address).first()
        
        if not self._sensor:
            RuntimeError("Нет датчика")
        
        self._daily_report = self.session.query(DailyReport).filter(
            and_(
                DailyReport.sensor_id==self._sensor.id,
                func.date(DailyReport.date)==self._date
            )
        ).first()
        
        welding_wire_diameter   = self.session.query(WeldingWireDiameter).filter(WeldingWireDiameter.id==self._daily_report.welding_wire_diameter_id).first()
        weld_metal              = self.session.query(WeldMetal).filter(WeldMetal.id==self._daily_report.weld_metal_id).first()
        welding_gas             = self.session.query(WeldingGas).filter(WeldingGas.id==self._daily_report.welding_gas_id).first()
        
        self._welding_process_parameters = None
        if self._daily_report:
            self._welding_process_parameters = WeldingProcessParameters(
                welding_wire_diameter.diameter,
                metal_density=weld_metal.density,
                metal_type=weld_metal.steel_name,
                gas_type=welding_gas.name
            )
        
        self._measurements = self.session.query(Measurement).filter(
            and_(
                Measurement.sensor_id==self._sensor.id,
                func.date(Measurement.utc_time)==self._date
            )
        ).all()
        
        
    @property
    def is_there_data(self) -> bool:
        return self._daily_report and self._measurements != []
    
    @property
    def measurements(self) -> List[Measurement]:
        return self._measurements

    @property
    def welding_process_parameters(self) -> WeldingProcessParameters:
        return self._welding_process_parameters
        
        

class _Converter(ABC):
    def __init__(self, mac_address: str, date: date, extension: str, session_=session, lazy_loading=True) -> None:
        self._date: str         = date
        self._mac_address: str  = mac_address
        self._extension: str    = extension
        self._lazy_loading: bool = lazy_loading
        self.session      = session_
        

        self._did_data_load = False
        
        self._data_store = DataBaseDataStore(
            mac_address, date, self.session
        ) if self._lazy_loading else None
    
    @property    
    def name_file(self) -> str:
        return self._mac_address + "-" +  self._date.strftime("%m-%d-%Y") + '.' + self._extension
    
    @property
    def data_store(self) -> DataBaseDataStore:
        return self._data_store
    
    @abstractmethod
    def load_from_DB(self) -> bool:
        return self._data_store.is_there_data if self._lazy_loading else False
    
    @abstractmethod
    def creat_file(self) -> None:
        pass
    
    @abstractmethod
    def save(self, path: Path) -> None:
        pass