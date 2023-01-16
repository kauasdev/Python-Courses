km = float(input("How many kilometers to trave: "))

if km < 200 or km == 200:
    travel_value = int(km) * 0.5
    print(f"The cost of the trip will be ${travel_value}")
else:
    travel_value = int(km) * 0.45
    print(f"The cost of the trip will be ${travel_value}")