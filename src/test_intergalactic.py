import unittest

from intergalactic import TransportShip, Passenger


class TestIntergalactic(unittest.TestCase):
    def test_ObjectOrientedProgramming_add_passenger(self):
        falcon = TransportShip("Millenium Falcon", 45, 128, 4)
        falcon.add_passenger(Passenger("Luke", "Endor", "Naboo", "Nathan"))
        falcon.add_passenger(Passenger("Porg", "Jakku", "Ilum", "Hoobe,Kool"))

        self.assertEqual(
            falcon.group_of_passengers,
            [
                Passenger("Luke", "Endor", "Naboo", "Nathan"),
                Passenger("Porg", "Jakku", "Ilum", "Hoobe,Kool"),
            ],
        )

    def test_Algorithms_total_passenger_in_group(self):
        falcon = TransportShip("Millenium Falcon", 45, 128, 31)
        falcon.add_passenger(Passenger("Luke", "Endor", "Naboo", ["Nathan"]))
        falcon.add_passenger(
            Passenger("Porg", "Jakku", "Ilum", ["Hoobe", "Kool"])
        )
        falcon.add_passenger(Passenger("Anakin", "Jakku", "Naboo"))
        falcon.add_passenger(
            Passenger(
                "Anni", "Jakku", "Ilum", ["Solo", "Han", "Mace", "Windu"]
            )
        )

        self.assertEqual(falcon.total_passenger_in_group("Porg"), 3)

    def test___SL___calculate_fare(self):
        falcon = TransportShip(
            ship_type="Millenium Falcon",
            min_fare=45.50,
            max_distance=12,
            capacity=7,
        )
        falcon.add_passenger(Passenger("Luke", "Endor", "Naboo", ["Nathan"]))
        falcon.add_passenger(
            Passenger("Porg", "Jakku", "Ilum", ["Hoobe", "Kool"])
        )
        falcon.add_passenger(Passenger("Anakin", "Jakku", "Naboo"))
        falcon.add_passenger(
            Passenger(
                "Anni", "Jakku", "Ilum", ["Solo", "Han", "Mace", "Windu"]
            )
        )
        falcon.add_passenger(Passenger("Darth", "Jakku", "Naboo", "Vader"))

        self.assertEqual(falcon.calculate_fare("Luke"), 67.07)

    def test___SL___calculate_group_fare(self):
        falcon = TransportShip(
            ship_type="Millenium Falcon",
            min_fare=5.5,
            max_distance=14,
            capacity=7,
        )
        falcon.add_passenger(
            Passenger(
                "Anni", "Jakku", "Ilum", ["Solo", "Han", "Mace", "Windu"]
            )
        )

        self.assertEqual(falcon.calculate_group_fare("anni"), 30.8)

    def test___SL___calculate_distance_(self):
        falcon = TransportShip("Millenium Falcon", 5.5, 14, 7)

        self.assertEqual(falcon.get_distance("Mon Cala", "Ilum"), 43.0)

    def test___SL___calculate_distance_reverse(self):
        falcon = TransportShip("Millenium Falcon", 5.5, 14, 7)

        self.assertEqual(falcon.get_distance("ryloth", "Jakku"), 43.5)
