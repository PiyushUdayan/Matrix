import re


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
elements = []
result=''
for i in range(m):
    for w in matrix:
        elements.append(w[i])
result = "".join(elements)
print(re.sub(r'\b[^a-zA-Z0-9]+\b',r' ',result))