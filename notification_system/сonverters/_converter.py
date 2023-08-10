from datetime import date

class _Converter:
    def __init__(self, mac_address: str, date: date, extension: str) -> None:
        self._date = date
        self._mac_address = mac_address
        
        self._name_file = self.__creat_name(extension)
        
        self._did_data_load = False
    
    def __creat_name(self, extension: str) -> str:
        return self._mac_address + "#" +  self._date.strftime("%m-%d-%Y") + '.' + extension