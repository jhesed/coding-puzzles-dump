import math

G = 9.81


def furious_chicken(
    initial_velocity: int, angle_in_degrees: int, time: float
) -> tuple:
    angle_in_degrees = math.radians(angle_in_degrees)

    x = initial_velocity * math.cos(angle_in_degrees) * time
    y = (initial_velocity * math.sin(angle_in_degrees) * time) - (
        0.5 * G * (time**2)
    )

    return round(x), round(y)
