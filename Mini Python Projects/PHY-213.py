import math

initial_velocity = int(input("What is the Initial Velocity? : "))
angle = int(input("What is the Angle? : "))

Range = ((initial_velocity**2) * (math.sin(math.radians(2*angle)))) / 9.8
Height = ((initial_velocity**2) * ((math.sin(math.radians(angle)))**2)) / (2*9.8)

print(f"The Range is {round(Range,2)} and the Height is {round(Height, 2)}")