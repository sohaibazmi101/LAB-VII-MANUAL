readings = [22.5, 23.1, 20.9, 24.0, 21.5, 19.8, 26.2, 23.5]
fahrenheit_readings = [c * 1.8 + 32 for c in readings]
hotdays = [c for c in readings if c > 23.0]
hot_days = []
for c in readings:
    if c > 23.0:
        hot_days.append(c)
print("Fahrenheit Readings: ",fahrenheit_readings)
print("Hot Days Using comprehension: ", hotdays)
print("Hot days using for loop: ",hot_days)