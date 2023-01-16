car_speed = float(input("What's the speed of the car: "))

if car_speed > 80:
    speeding = car_speed - 80
    fine_amount = int(speeding) * 7

    print(f"You were fined ${fine_amount}")
else:
    print("Drive slowly always...")