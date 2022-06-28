s = input()

s_letters = dict()
t_letters = dict()

for i in str(s):
    if i not in s_letters.keys():
        s_letters[i] = 1
    else:
        s_letters[i] = int(s_letters[i]) + 1

print(s_letters)

        