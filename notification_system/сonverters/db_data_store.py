from datetime import date
from typing import List

from sqlalchemy import and_, func

from notification_system.models import (
    Sensor, DailyReport, Measurement, 
    WeldingGas, WeldingWireDiameter, WeldMetal)




class WeldingProcessParameters:
    def __init__(self, wire_diameter: float, metal_density: float, metal_type: str, gas_type: str) -> None:
        self.wire_diameter: float   = wire_diameter
        self.metal_density: float   = metal_density
        self.metal_type:    str     = metal_type
        self.gas_type:      str     = gas_type
    

class DataBaseDataStore:
    
    def __init__(self, mac_address: str, date: date, session) -> None:
        self._sensor                        = session.query(Sensor).filter(Sensor.mac_address==mac_address).first()
        self._welding_process_parameters    = None
        
        if not self._sensor:
            RuntimeError(f"Датчик с данным MAC-адрессом {mac_address} не найден.")
        
        self._daily_report = session.query(DailyReport).filter(
            and_(
                DailyReport.sensor_id==self._sensor.id,
                func.date(DailyReport.date)==date
            )
        ).first()
        
        
        if self._daily_report:
            welding_wire_diameter   = session.query(WeldingWireDiameter).filter(WeldingWireDiameter.id==self._daily_report.welding_wire_diameter_id).first()
            weld_metal              = session.query(WeldMetal).filter(WeldMetal.id==self._daily_report.weld_metal_id).first()
            welding_gas             = session.query(WeldingGas).filter(WeldingGas.id==self._daily_report.welding_gas_id).first()
            
            self._welding_process_parameters = WeldingProcessParameters(
                welding_wire_diameter.diameter,
                metal_density=weld_metal.density,
                metal_type=weld_metal.steel_name,
                gas_type=welding_gas.name)
        
        self._measurements = session.query(Measurement).filter(
            and_(
                Measurement.sensor_id==self._sensor.id,
                func.date(Measurement.utc_time)==date
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