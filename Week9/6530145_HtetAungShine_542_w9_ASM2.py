def DistanceConversion(input):
    distance = float(input[:-2])
    unit = input[-2:]
    if unit == 'mi':
        converted_distance = distance * 1.609344
        converted_unit = 'km'
    elif unit == 'km':
        converted_distance = distance / 1.609344
        converted_unit = 'mi'
    return distance, converted_distance, unit, converted_unit
userInput = input('Enter a distance (in km or mi) : ')
distance, converted_distance, unit, converted_unit = DistanceConversion(userInput)
print(f'{distance} {unit} is equal to {converted_distance:.2f} {converted_unit}')