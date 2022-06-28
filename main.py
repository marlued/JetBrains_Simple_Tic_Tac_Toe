user_input = input().strip()

as_list = list(user_input)

line_1 = " ".join(as_list[:3])
line_2 = " ".join(as_list[3:6])
line_3 = " ".join(as_list[6:])

border = '---------'

print(border)
print(f'| {line_1} |')
print(f'| {line_2} |')
print(f'| {line_3} |')
print(border)
