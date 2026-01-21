class Distance:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value} {self.unit}"

    def _to_meters(self):
        if self.unit == 'meters':
            return self.value
        elif self.unit == 'kilometers':
            return self.value * 1000
        elif self.unit == 'cm':
            return self.value / 100
        else:
            raise ValueError("Unsupported unit")

    def __add__(self, other):
        meters = self._to_meters()
        meters += other._to_meters()

        return Distance(meters, 'meters')

d1 = Distance(10, 'kilometers')
d2 = Distance(500, 'meters')
print(d1 + d2)
