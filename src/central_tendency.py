import math


class Stat:
    def __init__(self, data: list):
        self.data = sorted(data)

    def mean(self):
        total = 0
        for n in self.data:
            total += n
        return total / len(self.data)

    def median(self) -> int:
        data_length = len(self.data)

        middle_element = self.data[int(math.floor(data_length / 2))]
        if data_length % 2 != 0:
            # odd number of elements, return the middle
            return middle_element

        next_to_middle_element = self.data[
            int(math.floor(data_length / 2)) - 1
        ]
        return (middle_element + next_to_middle_element) / 2

    def mode(self) -> list:
        occurrence = {}
        for num in self.data:
            if num not in occurrence:
                occurrence[num] = 0
            occurrence[num] += 1

        max_occurrence = max(occurrence.values())
        if max_occurrence == 1:
            return []

        values = []
        for key, value in occurrence.items():
            if value == max_occurrence:
                values.append(key)
        return values

    def range(self):
        return self.data[-1] - self.data[0]
