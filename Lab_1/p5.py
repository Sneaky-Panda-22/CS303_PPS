speed_car1 = int(input("Enter car1 speed(km/hr): "))
speed_car2 = int(input("Enter car2 speed(km/hr): "))
distance = int(input("Enter initial dist btn cars(km): "))
fly_speed = int(input("Enter fly speed(km/hr): "))

time = distance/(speed_car1 + speed_car2)
fly_dist_travelled = time * fly_speed

print(f"Dist travelled by fly: {fly_dist_travelled:.2f} km.")