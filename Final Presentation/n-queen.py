# 定義
def dfs(t):
    global ans # 令 ans 為全域變數
    if t > N:
        ans += 1 # 答案數加一
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                print('Q' if j == x[i] else 'x', end='\n' if j == N else '')
        print('')
    else: 
        for i in range(1, N + 1):
            ok = True
            x[t]= i
            for j in range(1, t):
                if(x[t] == x[j] or t+x[t] == j+x[j] or t-x[t] == j-x[j]):
                    ok = False
                    break
            if(ok): dfs(t + 1)


print("請輸入要解決幾皇后問題：", end='')
N = int(input(""))
x = [i for i in range(N + 1)]
ans = 0 # 答案數初始為 0
dfs(1) # 從第一層開始判斷
print("共有 ", ans, " 組解")

