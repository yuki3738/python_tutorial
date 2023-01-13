x = int(input("整数をいれてください:"))
if x < 0:
    x = 0
    print('負数は0とする')
elif x == 0:
    print('ゼロ')
elif x == 1:
    print('1つ')
else:
    print('もっと')
