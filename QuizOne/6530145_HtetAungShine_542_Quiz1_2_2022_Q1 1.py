mpm = float(input("Enter a wind speed in mile/min : "))
kph = mpm * 96.56
if mpm <= 0 or mpm == 1:
    print(f'Wind speed is {kph} km/hour and the wind condition is now calm.')
elif mpm > 1 and mpm < 25:
    print(f'Wind speed is {kph} km/hour and the wind condition is now light')
elif mpm > 25 and mpm < 40:
    print(f'Wind speed is {kph} km/hour and the wind condition is now moderate')
elif mpm > 40 and mpm < 60:
    print(f'Wind speed is {kph} km/hour and the wind condition is now strong')
elif mpm > 60:
    print(f'Wind speed is {kph} km/hour and the wind condition is now extreme')
elif mpm < 0:
    print(f'Wrong input. Wimd speed must be a positive value')