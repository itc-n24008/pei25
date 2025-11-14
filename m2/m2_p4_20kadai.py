num = 5
list_b = []

while num <= 25:
    for i in range(num, num + 1):
        if i % 2 == 1:   # 奇数なら追加
            list_b.append(i)
    num += 1

print(sum(list_b))

