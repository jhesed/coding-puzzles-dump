from decimal import Decimal

ADDITIONAL_FARE_PER_LIGHT_YEAR = Decimal("0.03")


class TransportShip:
    def __init__(self, ship_type, min_fare, max_distance, capacity):
        self.ship_type = ship_type
        self.min_fare = min_fare
        self.max_distance = max_distance  # maximum distance for paying minumum fare (unit is in lightyears)
        self.capacity = capacity
        self.group_of_passengers = []
        self.map = [
            {"from": "Mon Cala", "to": "Alderaan", "distance": 25},
            {"from": "Alderaan", "to": "Coruscant", "distance": 3.3},
            {"from": "Coruscant", "to": "Ilum", "distance": 14.7},
            {"from": "Ilum", "to": "Jakku", "distance": 18},
            {"from": "Jakku", "to": "Endor", "distance": 9.2},
            {"from": "Endor", "to": "Hoth", "distance": 7},
            {"from": "Hoth", "to": "Mustafar", "distance": 4.3},
            {"from": "Mustafar", "to": "Dagobah", "distance": 4.8},
            {"from": "Dagobah", "to": "Malastre", "distance": 8.8},
            {"from": "Malastre", "to": "Naboo", "distance": 2.9},
            {"from": "Naboo", "to": "Ryloth", "distance": 6.5},
        ]

        # Custom attributes
        self.companions = {}
        self.dict_map = self.map_to_dict()
        self.reversed_dict_map = self.map_to_reversed_dict()

    def get_passenger(self, passenger_name: str):
        for passenger in self.group_of_passengers:
            if passenger.name.lower() == passenger_name.lower():
                return passenger

    def add_passenger(self, group_of_passenger):
        self.group_of_passengers.append(group_of_passenger)
        if group_of_passenger.companion_name:
            # TODO: Convert to Passenger?
            self.companions[
                group_of_passenger.name.lower()
            ] = group_of_passenger.companion_name

    def total_passenger_in_group(self, passenger_name):
        passenger_name = passenger_name.lower()

        for passenger in self.group_of_passengers:
            if passenger.normalized_name == passenger_name:

                if not self.companions[passenger_name]:
                    return 1  # No companion
                return 1 + len(self.companions[passenger_name])

        # find and return total passengers given the passenger name. Name is case insensitive.

    def map_to_dict(self) -> dict:
        dict_map = {}
        for item in self.map:
            dict_map[item["from"].lower()] = {
                "from": item["from"].lower(),
                "to": item["to"].lower(),
                "distance": item["distance"],
            }
        return dict_map

    def map_to_reversed_dict(self) -> dict:
        dict_map = {}
        for item in self.map:
            dict_map[item["to"].lower()] = {
                "from": item["to"].lower(),
                "to": item["from"].lower(),
                "distance": item["distance"],
            }
        return dict_map

    def get_distance(self, origin, destination) -> float:

        origin = origin.lower()
        destination = destination.lower()

        if (
            origin not in self.dict_map.keys()
            and origin not in self.reversed_dict_map.keys()
        ):
            return 0
        if (
            destination not in self.dict_map.keys()
            and destination not in self.reversed_dict_map.keys()
        ):
            return 0

        if origin in self.dict_map.keys():
            source = self.dict_map
            other_source = self.reversed_dict_map
        else:
            source = self.reversed_dict_map
            other_source = self.dict_map

        try:
            return self._calc_distance(
                origin=origin.lower(), source=source, destination=destination
            )
        except:
            return self._calc_distance(
                origin=origin.lower(),
                source=other_source,
                destination=destination,
            )

    @staticmethod
    def _calc_distance(origin, source, destination):
        distance = 0.0
        current_origin = origin.lower()
        while True:
            distance += source[current_origin]["distance"]
            current_origin = source[current_origin]["to"]
            if current_origin == destination:
                return distance

    def calculate_fare(self, passenger_name):
        passenger = self.get_passenger(passenger_name=passenger_name)
        if not passenger:
            return None

        try:
            distance = Decimal(
                str(
                    self.get_distance(
                        origin=passenger.origin,
                        destination=passenger.destination,
                    )
                )
            )
        except:
            return 0

        if not distance:
            return 0

        distance_not_covered_by_min_fare = distance - Decimal(
            str(self.max_distance)
        )
        if distance_not_covered_by_min_fare < 0:
            return self.min_fare

        per_light_year_fare = ADDITIONAL_FARE_PER_LIGHT_YEAR * Decimal(
            str(self.min_fare)
        )

        additional_fare = (
            per_light_year_fare * distance_not_covered_by_min_fare
        )
        return float(round(Decimal(str(self.min_fare)) + additional_fare, 2))

    def calculate_group_fare(self, passenger_name):
        return self.calculate_fare(
            passenger_name=passenger_name
        ) * self.total_passenger_in_group(passenger_name=passenger_name)


class Passenger:
    def __init__(self, name, origin, destination, companion_name=None):
        self.name = name
        self.companion_name = (
            companion_name  # multiples names in a list; can be null
        )
        self.origin = origin
        self.destination = destination

        self.normalized_name = self.name.lower()

    def __eq__(self, other):
        ## do not delete this
        return (
            isinstance(other, Passenger)
            and self.name == other.name
            and self.origin == other.origin
            and self.destination == other.destination
            and self.companion_name == other.companion_name
        )
