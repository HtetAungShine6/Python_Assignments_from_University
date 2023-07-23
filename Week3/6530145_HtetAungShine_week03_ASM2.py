temperature = float(input("Enter Fahrenheit : "))
tempInCelsius = (5*(temperature-32))/9
if tempInCelsius >= 22:
    print(f'The temperature is {tempInCelsius} degreem Celsius.')
if tempInCelsius <= 22 and tempInCelsius > 0:
    print("Very cold indeed.")
else:
    print("Too cold to live.")