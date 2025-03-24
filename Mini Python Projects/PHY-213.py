import math

# initial_velocity = int(input("What is the Initial Velocity? : "))
# angle = int(input("What is the Angle? : "))

# Range = ((initial_velocity**2) * (math.sin(math.radians(2*angle)))) / 9.8
# Height = ((initial_velocity**2) * ((math.sin(math.radians(angle)))**2)) / (2*9.8)

# print(f"The Range is {round(Range,2)} and the Height is {round(Height, 2)}")

def projectile_motion(initial_velocity, angle):
    distance = ((initial_velocity**2) * (math.sin(math.radians(2*angle)))) / 9.8
    height = ((initial_velocity**2) * ((math.sin(math.radians(angle)))**2)) / (2*9.8)
    return distance, height

# for angle in range(25, 86, 10):
#     distance, height = projectile_motion(15, angle)
#     print(f"When Angle is {angle} \nThe Range is {round(distance,2)} and the Height is {round(height, 2)}")


for vi in range(5, 31, 5):
    distance, height = projectile_motion(vi, 45)
    print(f"When Initial Velcity is {vi}m/s \nThe Range is {round(distance,2)} and the Height is {round(height, 2)}")