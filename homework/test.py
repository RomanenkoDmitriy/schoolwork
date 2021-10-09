import random

plaers = ['Bob', 'Joi', 'Mik']


def play_raund():
    point = 0
    for item in range(3):
        point += random.randint(1, 6)
    return point

plaers_point = {}
for plaer in plaers:
    plaers_point[plaer] = play_raund()

points = []
for point in plaers_point.values():
    points.append(point)

max_point = max(points)

vin_plaers = []
for plaer, point in plaers_point.items():
    if point == max_point:
        vin_plaers.append({plaer: point})

print(f'У нас {len(vin_plaers)} победител(я): ')
for viner in vin_plaers:
    for plaer, point in viner.items():
        print(f'{plaer} point: {point}')