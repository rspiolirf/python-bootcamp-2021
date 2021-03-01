with open('devices.txt') as file:
    lines = file.read().splitlines()

result = [line.split(':') for line in lines]
print(result)