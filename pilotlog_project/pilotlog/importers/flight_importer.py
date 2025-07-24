from .base_importer import BaseImporter
from ..models import Flight, Aircraft, Airfield, Pilot
from datetime import datetime

class FlightImporter(BaseImporter):
    def get_model(self):
        return Flight

    def process(self):
        aircraft = Aircraft.objects.filter(guid=self.meta.get('AircraftCode')).first()
        departure_airfield = Airfield.objects.filter(guid=self.meta.get('DepCode')).first()
        arrival_airfield = Airfield.objects.filter(guid=self.meta.get('ArrCode')).first()
        pilot1 = Pilot.objects.filter(guid=self.meta.get('P1Code')).first()
        pilot2 = Pilot.objects.filter(guid=self.meta.get('P2Code')).first()
        pilot3 = Pilot.objects.filter(guid=self.meta.get('P3Code')).first()
        pilot4 = Pilot.objects.filter(guid=self.meta.get('P4Code')).first()

        flight_date = self.meta.get('DateUTC')
        if flight_date:
            flight_date = datetime.strptime(flight_date, '%Y-%m-%d').date()

        self.get_model().objects.update_or_create(
            guid=self.guid,
            defaults={
                'aircraft': aircraft,
                'departure_airfield': departure_airfield,
                'arrival_airfield': arrival_airfield,
                'pilot1': pilot1,
                'pilot2': pilot2,
                'pilot3': pilot3,
                'pilot4': pilot4,
                'flight_date': flight_date,
                'total_duration': self.meta.get('minTOTAL'),
                'remarks': self.meta.get('Remarks'),
                'pf': self.meta.get('PF', False),
                'pax': self.meta.get('Pax'),
                'fuel': self.meta.get('Fuel'),
                'deice': self.meta.get('DeIce', False),
                'route': self.meta.get('Route'),
                'today': self.meta.get('ToDay'),
                'minu1': self.meta.get('minU1'),
                'minu2': self.meta.get('minU2'),
                'minu3': self.meta.get('minU3'),
                'minu4': self.meta.get('minU4'),
                'minxc': self.meta.get('minXC'),
                'arrrwy': self.meta.get('ArrRwy'),
                'deprwy': self.meta.get('DepRwy'),
                'ldgday': self.meta.get('LdgDay'),
                'liftsw': self.meta.get('LiftSW'),
                'report': self.meta.get('Report'),
                'tagops': self.meta.get('TagOps'),
                'toedit': self.meta.get('ToEdit', False),
                'minair': self.meta.get('minAIR'),
                'mincop': self.meta.get('minCOP'),
                'minifr': self.meta.get('minIFR'),
                'minimt': self.meta.get('minIMT'),
                'minpic': self.meta.get('minPIC'),
                'minrel': self.meta.get('minREL'),
                'minsfr': self.meta.get('minSFR'),
                'dateutc': self.meta.get('DateUTC'),
                'hobbsin': self.meta.get('HobbsIn'),
                'holding': self.meta.get('Holding'),
                'pairing': self.meta.get('Pairing'),
                'signbox': self.meta.get('SignBox'),
                'tonight': self.meta.get('ToNight'),
                'usernum': self.meta.get('UserNum'),
                'mindual': self.meta.get('minDUAL'),
                'minexam': self.meta.get('minEXAM'),
                'crewlist': self.meta.get('CrewList'),
                'datebase': self.meta.get('DateBASE'),
                'fuelused': self.meta.get('FuelUsed'),
                'hobbsout': self.meta.get('HobbsOut'),
                'ldgnight': self.meta.get('LdgNight'),
                'nextpage': self.meta.get('NextPage', False),
                'tagdelay': self.meta.get('TagDelay'),
                'training': self.meta.get('Training'),
                'userbool': self.meta.get('UserBool', False),
                'usertext': self.meta.get('UserText'),
                'mininstr': self.meta.get('minINSTR'),
                'minnight': self.meta.get('minNIGHT'),
                'minpicus': self.meta.get('minPICUS'),
                'mintotal': self.meta.get('minTOTAL'),
                'arroffset': self.meta.get('ArrOffset'),
                'datelocal': self.meta.get('DateLOCAL'),
                'depoffset': self.meta.get('DepOffset'),
                'taglaunch': self.meta.get('TagLaunch'),
                'taglesson': self.meta.get('TagLesson'),
                'totimeutc': self.meta.get('ToTimeUTC'),
                'arrtimeutc': self.meta.get('ArrTimeUTC'),
                'baseoffset': self.meta.get('BaseOffset'),
                'deptimeutc': self.meta.get('DepTimeUTC'),
                'ldgtimeutc': self.meta.get('LdgTimeUTC'),
                'fuelplanned': self.meta.get('FuelPlanned'),
                'nextsummary': self.meta.get('NextSummary', False),
                'tagapproach': self.meta.get('TagApproach'),
                'arrtimesched': self.meta.get('ArrTimeSCHED'),
                'deptimesched': self.meta.get('DepTimeSCHED'),
                'flightnumber': self.meta.get('FlightNumber'),
                'flightsearch': self.meta.get('FlightSearch'),
                'record_modified': self.meta.get('Record_Modified'),
            }
        )
