from notification_system.сonverters.to_excel import MeasurementsToExcelConverter
from datetime import date
from pathlib import Path

if __name__ == '__main__':
    mc = MeasurementsToExcelConverter("ZIT-RW", date=date(2023, 8, 22))
    print(mc.load_from_DB())
    if mc.load_from_DB():
        mc.creat_file()
        mc.save(Path('.'))