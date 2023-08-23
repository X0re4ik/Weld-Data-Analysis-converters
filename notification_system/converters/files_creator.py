from typing import List
from datetime import date
from pathlib import Path


from notification_system.models import session, Sensor
from notification_system.converters.to_excel import MeasurementsToExcelConverter, _Converter


class FilesCreator:

    CONVERTORS: List[_Converter] = [
        MeasurementsToExcelConverter
    ]
    
    
    def __init__(self, root: Path, session=session) -> None:
        if not root.exists():
            raise FileNotFoundError(f"Папки по следующему пути не найдено {root.absolute()}")
        self._root = root
        self._session = session
        
    def creat_reports(self, date: date):
        for sensor in self._session.query(Sensor).filter().all():
            mac_address: str = sensor.mac_address
            self._creat_report(mac_address, date)
                
    
    def _creat_report(self, mac_address: str, date: date):
        for cls_convertor in self.__class__.CONVERTORS:
            new_dir_with_mac_address = Path.joinpath(self._root, mac_address)
            new_dir_with_mac_address.mkdir(exist_ok=True)
            
            to_converter = cls_convertor(mac_address, date)
            if to_converter.load_from_DB():
                to_converter.creat_file()
                to_converter.save(path=new_dir_with_mac_address)
    
