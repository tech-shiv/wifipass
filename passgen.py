# input name and dob
name = input('Enter name: ')
dob = int(input('Date of Birth (DDMMYYYY) '))
# length of Name and allocation of special characters
char = [')', '!', '@', '#', '$', '%', '^', '&', '*', '(']
list_a = []

# length of dob
res = 0
while dob > 0:
    r = dob % 10
    res = res + r
    dob = dob // 10
dob = res

if res > 9:
    res = 0
    while dob > 0:
        r = dob % 10
        res = res + r
        dob = dob // 10
    c1 = res

# print(name_len)
for element in name[1:: 2]:
    # print(element, end =' ')
    list_a.append(element)

# pick even Alphabets
list_a.sort()
c2 = list_a[0]

name_len = len(name)
c4 = len(name)
if name_len > 9:
    c4 -= 9
    val = 0
    while name_len > 0:
        rem = name_len % 10
        val = val + rem
        name_len = name_len // 10

else:
    c4 = len(name)
    val = name_len
c3 = char[val]

# Final result
print(f'{c1}{c2}{c3}{c4}')
