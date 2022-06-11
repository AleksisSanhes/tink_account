f = open('prob.txt', encoding="utf-8")
first = f.read().split('\n')
fic = {}
print(first)

for i in first:
    print(i)
f.close()