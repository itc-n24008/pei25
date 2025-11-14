num = 3
list_a = [] # からのリストを作成
while num < 5: # numが５未満の時繰り返す
    for i in range(num, 10, 3): # num=3の場合、3から１０まで３つおき、つまり[3, 6, 9]
        i -= 6 # i-6をiに代入
        list_a.append(i) # list_aにiを追加
    num += 1 # numを１増やす
print(sum(list_a)) # 合計を出力する
