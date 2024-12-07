def mutate_string(string,position,character):
    char = string[position]
    return string[:position] + character +string[:position+1]

s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)