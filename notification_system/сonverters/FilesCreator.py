from typing import List
from datetime import date
from pathlib import Path


from notification_system.models import Sensor
from notification_system.сonverters.to_excel import MeasurementsToExcelConverter


class FilesCreator:

    CONVERTORS: List = [
        MeasurementsToExcelConverter
    ]
    
    
    def __init__(self, session, root: Path) -> None:
        if not root.exists():
            raise FileNotFoundError(f"Папки по следующему пути не найдено {root.absolute()}")
        self._root = root
        self._session = session
        
    def creat_reports(self, date: date):
        sensors = self._session.query(Sensor).filter().all()
        for sensor in sensors:
            mac_address: str = sensor.mac_address
            self.creat_report(mac_address, date)
                
    
    def creat_report(self, mac_address: str, date: date):
        for cls_convertor in self.__class__.CONVERTORS:
            new_dir_with_mac_address = Path.joinpath(self._root, mac_address)
            new_dir_with_mac_address.mkdir(exist_ok=True)
            
            to_converter = cls_convertor(mac_address, date)
            if to_converter.load_from_DB(self._session):
                to_converter.write_measurements()
                to_converter.save(path=new_dir_with_mac_address)
    
