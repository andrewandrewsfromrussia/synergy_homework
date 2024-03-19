result = {}

for key in range(10, -6, -1):
    value = key ** key
    result[key] = value

print(result)