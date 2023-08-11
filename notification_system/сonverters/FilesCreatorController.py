from multiprocessing import Process
from pathlib import Path

from datetime import datetime, time, date, timedelta
from notification_system.models import session
from notification_system.сonverters.FilesCreator import FilesCreator


class FilesCreatorController(Process):
    
    REPORTING_TIME = time(hour=9, minute=28, second=0)
    
    PATH_TO_FILE_DB = Path(r"C:\Users\Ferre\OneDrive\Документы\Xore4ik\ZIT-ReadWeld\db\sensors")
    
    def __init__(self) -> None:
        Process.__init__(self)
        
        self._did_current_day_record = False
        self._has_new_day_come = False
    
    def run(self):
        
        next_day = (datetime.now() + timedelta(days=1)).date()
        
        while True:
            current_date = date.today()
            
            if (datetime.now().time() > self.__class__.REPORTING_TIME) and not self._did_current_day_record:
                fc = FilesCreator(session, self.__class__.PATH_TO_FILE_DB)
                fc.creat_reports(current_date)
                self._did_current_day_record = True
            
            self._has_new_day_come = (next_day == current_date)
            
            if self._has_new_day_come and self._did_current_day_record:
                self._has_new_day_come = False
                self._did_current_day_record = False
                next_day = current_date + timedelta(days=1) 