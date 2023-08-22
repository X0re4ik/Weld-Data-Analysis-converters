from datetime import date
from pathlib import Path
from abc import ABC, abstractmethod

from notification_system.models import session

from notification_system.models import Sensor, DailyReport, Measurement, WeldingGas, WeldingWireDiameter, WeldMetal
from sqlalchemy import and_, func


from typing import List
from notification_system.converters.db_data_store import DataBaseDataStore

class _Converter(ABC):
    def __init__(self, mac_address: str, date: date, extension: str, session_=session, lazy_loading=True) -> None:
        self._date          : str   = date
        self._mac_address   : str   = mac_address
        self._extension     : str   = extension
        self._lazy_loading  : bool  = lazy_loading
        self.session                = session_
        
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