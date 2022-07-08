test = {1: 3, 3: 5, 2: 1}

dict(sorted(test.items(), key=lambda item: item[1]))

print(test)