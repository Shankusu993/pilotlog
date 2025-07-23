import json
from django.core.management.base import BaseCommand
from pilotlog.models import Aircraft, Airfield, Pilot, Flight
from datetime import datetime

class Command(BaseCommand):
    help = 'Import data from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='The path to the JSON file to import.')

    def handle(self, *args, **options):
        with open(options['json_file'], 'r') as f:
            data = json.load(f)

        # First pass: import Aircraft, Airfield, Pilot
        for record in data:
            table_name = record['table'].lower()
            meta = record['meta']
            guid = record['guid']

            if table_name == 'aircraft':
                Aircraft.objects.update_or_create(
                    guid=guid,
                    defaults={
                        'make': meta.get('Make'),
                        'model': meta.get('Model'),
                        'reference': meta.get('Reference'),
                        'fin': meta.get('Fin'),
                        'sea': meta.get('Sea', False),
                        'tmg': meta.get('TMG', False),
                        'efis': meta.get('Efis', False),
                        'fnpt': meta.get('FNPT'),
                        'run2': meta.get('Run2', False),
                        'aircraft_class': meta.get('Class'),
                        'power': meta.get('Power'),
                        'seats': meta.get('Seats'),
                        'active': meta.get('Active', True),
                        'kg5700': meta.get('Kg5700', False),
                        'rating': meta.get('Rating'),
                        'company': meta.get('Company'),
                        'complex': meta.get('Complex', False),
                        'condlog': meta.get('CondLog'),
                        'favlist': meta.get('FavList', False),
                        'category': meta.get('Category'),
                        'highperf': meta.get('HighPerf', False),
                        'submodel': meta.get('SubModel'),
                        'aerobatic': meta.get('Aerobatic', False),
                        'refsearch': meta.get('RefSearch'),
                        'tailwheel': meta.get('Tailwheel', False),
                        'defaultapp': meta.get('DefaultApp'),
                        'defaultlog': meta.get('DefaultLog'),
                        'defaultops': meta.get('DefaultOps'),
                        'devicecode': meta.get('DeviceCode'),
                        'aircraftcode': meta.get('AircraftCode'),
                        'defaultlaunch': meta.get('DefaultLaunch'),
                        'record_modified': meta.get('Record_Modified'),
                    }
                )
            elif table_name == 'airfield':
                Airfield.objects.update_or_create(
                    guid=guid,
                    defaults={
                        'name': meta.get('AFName'),
                        'icao_code': meta.get('AFICAO'),
                        'iata_code': meta.get('AFIATA'),
                        'latitude': meta.get('Latitude'),
                        'longitude': meta.get('Longitude'),
                        'afcat': meta.get('AFCat'),
                        'afcode': meta.get('AFCode'),
                        'afcountry': meta.get('AFCountry'),
                        'notesuser': meta.get('NotesUser'),
                        'regionuser': meta.get('RegionUser'),
                        'elevationft': meta.get('ElevationFT'),
                        'record_modified': meta.get('Record_Modified'),
                    }
                )
            elif table_name == 'pilot':
                Pilot.objects.update_or_create(
                    guid=guid,
                    defaults={
                        'name': meta.get('PilotName'),
                        'email': meta.get('PilotEMail'),
                        'company': meta.get('Company'),
                        'active': meta.get('Active', True),
                        'notes': meta.get('Notes'),
                        'favlist': meta.get('FavList', False),
                        'userapi': meta.get('UserAPI'),
                        'facebook': meta.get('Facebook'),
                        'linkedin': meta.get('LinkedIn'),
                        'pilotref': meta.get('PilotRef'),
                        'pilotcode': meta.get('PilotCode'),
                        'pilotphone': meta.get('PilotPhone'),
                        'certificate': meta.get('Certificate'),
                        'phonesearch': meta.get('PhoneSearch'),
                        'pilotsearch': meta.get('PilotSearch'),
                        'rosteralias': meta.get('RosterAlias'),
                        'record_modified': meta.get('Record_Modified'),
                    }
                )

        # Second pass: import Flights
        for record in data:
            table_name = record['table'].lower()
            meta = record['meta']
            guid = record['guid']

            if table_name == 'flight':
                aircraft = Aircraft.objects.filter(guid=meta.get('AircraftCode')).first()
                departure_airfield = Airfield.objects.filter(guid=meta.get('DepCode')).first()
                arrival_airfield = Airfield.objects.filter(guid=meta.get('ArrCode')).first()
                pilot1 = Pilot.objects.filter(guid=meta.get('P1Code')).first()
                pilot2 = Pilot.objects.filter(guid=meta.get('P2Code')).first()
                pilot3 = Pilot.objects.filter(guid=meta.get('P3Code')).first()
                pilot4 = Pilot.objects.filter(guid=meta.get('P4Code')).first()

                flight_date = meta.get('DateUTC')
                if flight_date:
                    flight_date = datetime.strptime(flight_date, '%Y-%m-%d').date()

                Flight.objects.update_or_create(
                    guid=guid,
                    defaults={
                        'aircraft': aircraft,
                        'departure_airfield': departure_airfield,
                        'arrival_airfield': arrival_airfield,
                        'pilot1': pilot1,
                        'pilot2': pilot2,
                        'pilot3': pilot3,
                        'pilot4': pilot4,
                        'flight_date': flight_date,
                        'total_duration': meta.get('minTOTAL'),
                        'remarks': meta.get('Remarks'),
                        'pf': meta.get('PF', False),
                        'pax': meta.get('Pax'),
                        'fuel': meta.get('Fuel'),
                        'deice': meta.get('DeIce', False),
                        'route': meta.get('Route'),
                        'today': meta.get('ToDay'),
                        'minu1': meta.get('minU1'),
                        'minu2': meta.get('minU2'),
                        'minu3': meta.get('minU3'),
                        'minu4': meta.get('minU4'),
                        'minxc': meta.get('minXC'),
                        'arrrwy': meta.get('ArrRwy'),
                        'deprwy': meta.get('DepRwy'),
                        'ldgday': meta.get('LdgDay'),
                        'liftsw': meta.get('LiftSW'),
                        'report': meta.get('Report'),
                        'tagops': meta.get('TagOps'),
                        'toedit': meta.get('ToEdit', False),
                        'minair': meta.get('minAIR'),
                        'mincop': meta.get('minCOP'),
                        'minifr': meta.get('minIFR'),
                        'minimt': meta.get('minIMT'),
                        'minpic': meta.get('minPIC'),
                        'minrel': meta.get('minREL'),
                        'minsfr': meta.get('minSFR'),
                        'dateutc': meta.get('DateUTC'),
                        'hobbsin': meta.get('HobbsIn'),
                        'holding': meta.get('Holding'),
                        'pairing': meta.get('Pairing'),
                        'signbox': meta.get('SignBox'),
                        'tonight': meta.get('ToNight'),
                        'usernum': meta.get('UserNum'),
                        'mindual': meta.get('minDUAL'),
                        'minexam': meta.get('minEXAM'),
                        'crewlist': meta.get('CrewList'),
                        'datebase': meta.get('DateBASE'),
                        'fuelused': meta.get('FuelUsed'),
                        'hobbsout': meta.get('HobbsOut'),
                        'ldgnight': meta.get('LdgNight'),
                        'nextpage': meta.get('NextPage', False),
                        'tagdelay': meta.get('TagDelay'),
                        'training': meta.get('Training'),
                        'userbool': meta.get('UserBool', False),
                        'usertext': meta.get('UserText'),
                        'mininstr': meta.get('minINSTR'),
                        'minnight': meta.get('minNIGHT'),
                        'minpicus': meta.get('minPICUS'),
                        'mintotal': meta.get('minTOTAL'),
                        'arroffset': meta.get('ArrOffset'),
                        'datelocal': meta.get('DateLOCAL'),
                        'depoffset': meta.get('DepOffset'),
                        'taglaunch': meta.get('TagLaunch'),
                        'taglesson': meta.get('TagLesson'),
                        'totimeutc': meta.get('ToTimeUTC'),
                        'arrtimeutc': meta.get('ArrTimeUTC'),
                        'baseoffset': meta.get('BaseOffset'),
                        'deptimeutc': meta.get('DepTimeUTC'),
                        'ldgtimeutc': meta.get('LdgTimeUTC'),
                        'fuelplanned': meta.get('FuelPlanned'),
                        'nextsummary': meta.get('NextSummary', False),
                        'tagapproach': meta.get('TagApproach'),
                        'arrtimesched': meta.get('ArrTimeSCHED'),
                        'deptimesched': meta.get('DepTimeSCHED'),
                        'flightnumber': meta.get('FlightNumber'),
                        'flightsearch': meta.get('FlightSearch'),
                        'record_modified': meta.get('Record_Modified'),
                    }
                )

        self.stdout.write(self.style.SUCCESS('Successfully imported data.'))
