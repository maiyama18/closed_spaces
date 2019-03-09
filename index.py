from radix import convert_number, num_closed_spaces

k, L, H = map(int, input().split())

sum_closed_spaces = 0
for i in range(L, H + 1):
    num_str = convert_number(i, k)
    sum_closed_spaces += num_closed_spaces(num_str)

print(sum_closed_spaces)
