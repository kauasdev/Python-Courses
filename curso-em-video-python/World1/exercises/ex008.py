meters = float(input("Enter the measurement in meters: "))

divider = '=' * 20

km = meters / 1000
hm = meters / 100
dam = meters / 10
dm = meters * 10
cm = meters * 100
mm = meters * 1000

print('{}\nMeters: {} \n\nKm: {} \nHm: {} \nDam: {} \nDm: {} \nCm: {} \nMm: {} \n{} '.format(divider, meters, km, hm, dam, dm, cm, mm, divider))