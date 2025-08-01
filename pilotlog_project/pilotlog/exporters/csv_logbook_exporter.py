import csv
from .base_exporter import BaseExporter
from ..models import Aircraft, Flight


class CsvLogbookExporter(BaseExporter):
    """Exports data to a CSV file in the logbook format."""

    def export(self, file_path):
        """
        Exports the data to a CSV file.

        Args:
            file_path (str): The path to the output CSV file.
        """
        with open(file_path, "w", newline="") as f:
            writer = csv.writer(f)

            # Write Aircraft Table
            writer.writerow(
                [
                    "Aircraft Table",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                ]
            )
            writer.writerow(
                [
                    "AircraftID",
                    "EquipmentType",
                    "TypeCode",
                    "Year",
                    "Make",
                    "Model",
                    "Category",
                    "Class",
                    "GearType",
                    "EngineType",
                    "Complex",
                    "HighPerformance",
                    "Pressurized",
                    "TAA",
                ]
            )
            for aircraft in Aircraft.objects.all():
                writer.writerow(
                    [
                        aircraft.reference,
                        "",  # EquipmentType - not in our model
                        "",  # TypeCode - not in our model
                        "",  # Year - not in our model
                        aircraft.make,
                        aircraft.model,
                        aircraft.category,
                        aircraft.aircraft_class,
                        "",  # GearType - not in our model
                        "",  # EngineType - not in our model
                        aircraft.complex,
                        aircraft.highperf,
                        "",  # Pressurized - not in our model
                        "",  # TAA - not in our model
                    ]
                )

            writer.writerow([])
            writer.writerow([])

            # Write Flights Table
            writer.writerow(
                [
                    "Flights Table",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                ]
            )
            writer.writerow(
                [
                    "Date",
                    "AircraftID",
                    "From",
                    "To",
                    "Route",
                    "TimeOut",
                    "TimeOff",
                    "TimeOn",
                    "TimeIn",
                    "OnDuty",
                    "OffDuty",
                    "TotalTime",
                    "PIC",
                    "SIC",
                    "Night",
                    "Solo",
                    "CrossCountry",
                    "NVG",
                    "NVGOps",
                    "Distance",
                    "DayTakeoffs",
                    "DayLandingsFullStop",
                    "NightTakeoffs",
                    "NightLandingsFullStop",
                    "AllLandings",
                    "ActualInstrument",
                    "SimulatedInstrument",
                    "HobbsStart",
                    "HobbsEnd",
                    "TachStart",
                    "TachEnd",
                    "Holds",
                    "Approach1",
                    "Approach2",
                    "Approach3",
                    "Approach4",
                    "Approach5",
                    "Approach6",
                    "DualGiven",
                    "DualReceived",
                    "SimulatedFlight",
                    "GroundTraining",
                    "InstructorName",
                    "InstructorComments",
                    "Person1",
                    "Person2",
                    "Person3",
                    "Person4",
                    "Person5",
                    "Person6",
                    "FlightReview",
                    "Checkride",
                    "IPC",
                    "NVGProficiency",
                    "FAA6158",
                    "[Text]CustomFieldName",
                    "[Numeric]CustomFieldName",
                    "[Hours]CustomFieldName",
                    "[Counter]CustomFieldName",
                    "[Date]CustomFieldName",
                    "[DateTime]CustomFieldName",
                    "[Toggle]CustomFieldName",
                    "PilotComments",
                ]
            )

            for flight in self.queryset:
                writer.writerow(
                    [
                        flight.flight_date,
                        flight.aircraft.reference if flight.aircraft else "",
                        (
                            flight.departure_airfield.name
                            if flight.departure_airfield
                            else ""
                        ),
                        flight.arrival_airfield.name if flight.arrival_airfield else "",
                        flight.route,
                        "",  # TimeOut
                        "",  # TimeOff
                        "",  # TimeOn
                        "",  # TimeIn
                        "",  # OnDuty
                        "",  # OffDuty
                        flight.total_duration,
                        flight.minpic,
                        flight.mincop,
                        flight.minnight,
                        "",  # Solo
                        flight.minxc,
                        "",  # NVG
                        "",  # NVGOps
                        "",  # Distance
                        flight.ldgday,  # DayTakeoffs
                        flight.ldgday,  # DayLandingsFullStop
                        flight.ldgnight,  # NightTakeoffs
                        flight.ldgnight,  # NightLandingsFullStop
                        (flight.ldgday or 0) + (flight.ldgnight or 0),  # AllLandings
                        flight.mininstr,  # ActualInstrument
                        flight.minimt,  # SimulatedInstrument
                        flight.hobbsout,
                        flight.hobbsin,
                        "",  # TachStart
                        "",  # TachEnd
                        flight.holding,
                        "",  # Approach1
                        "",  # Approach2
                        "",  # Approach3
                        "",  # Approach4
                        "",  # Approach5
                        "",  # Approach6
                        flight.mindual,  # DualGiven
                        "",  # DualReceived
                        "",  # SimulatedFlight
                        "",  # GroundTraining
                        "",  # InstructorName
                        "",  # InstructorComments
                        flight.pilot1.name if flight.pilot1 else "",
                        flight.pilot2.name if flight.pilot2 else "",
                        flight.pilot3.name if flight.pilot3 else "",
                        flight.pilot4.name if flight.pilot4 else "",
                        "",  # Person5
                        "",  # Person6
                        "",  # FlightReview
                        "",  # Checkride
                        "",  # IPC
                        "",  # NVGProficiency
                        "",  # FAA6158
                        "",  # [Text]CustomFieldName
                        "",  # [Numeric]CustomFieldName
                        "",  # [Hours]CustomFieldName
                        "",  # [Counter]CustomFieldName
                        "",  # [Date]CustomFieldName
                        "",  # [DateTime]CustomFieldName
                        "",  # [Toggle]CustomFieldName
                        flight.remarks,
                    ]
                )
