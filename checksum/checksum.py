
key = 0
while(key == 0):
    print("請輸入身分證字號：", end=" ")
    ID = input()


    #判斷字首的字母，並換算成加權數
    if ID[0].upper() == 'A':
        idNumber = 10
    elif ID[0].upper() == 'B':
        idNumber = 11
    elif ID[0].upper() == 'C':
        idNumber = 12
    elif ID[0].upper() == 'D':
        idNumber = 13
    elif ID[0].upper() == 'E':
        idNumber = 14
    elif ID[0].upper() == 'F':
        idNumber = 15
    elif ID[0].upper() == 'G':
        idNumber = 16
    elif ID[0].upper() == 'H':
        idNumber = 17
    elif ID[0].upper() == 'I':
        idNumber = 34
    elif ID[0].upper() == 'J':
        idNumber = 18
    elif ID[0].upper() == 'K':
        idNumber = 19
    elif ID[0].upper() == 'L':
        idNumber = 20
    elif ID[0].upper() == 'M':
        idNumber = 21
    elif ID[0].upper() == 'N':
        idNumber = 22
    elif ID[0].upper() == 'O':
        idNumber = 35
    elif ID[0].upper() == 'P':
        idNumber = 23
    elif ID[0].upper() == 'Q':
        idNumber = 24
    elif ID[0].upper() == 'R':
        idNumber = 25
    elif ID[0].upper() == 'S':
        idNumber = 26
    elif ID[0].upper() == 'T':
        idNumber = 27
    elif ID[0].upper() == 'U':
        idNumber = 28
    elif ID[0].upper() == 'V':
        idNumber = 29
    elif ID[0].upper() == 'W':
        idNumber = 32
    elif ID[0].upper() == 'X':
        idNumber = 30
    elif ID[0].upper() == 'Y':
        idNumber = 31
    else:
        idNumber = 33


    #數值乘上加權並加上檢查碼
    totalSum = 0
    for i in range(10):
        if i == 0:
            totalSum += int(idNumber / 10) * 1 
            totalSum += (idNumber % 10) * 9  
        elif i == 1:
            totalSum += (int(ID[i]) * 8)
        elif i == 2:
            totalSum += (int(ID[i]) * 7)
        elif i == 3:
            totalSum += (int(ID[i]) * 6)
        elif i == 4:
            totalSum += (int(ID[i]) * 5)
        elif i == 5:
            totalSum += (int(ID[i]) * 4)
        elif i == 6:
            totalSum += (int(ID[i]) * 3)
        elif i == 7:
            totalSum += (int(ID[i]) * 2)
        elif i == 8:
            totalSum += (int(ID[i]) * 1)
        else:
            totalSum += int(ID[i])


    #檢查和
    if totalSum % 10 == 0:
        print("正確的身分證字號")
        key = 1
    else:
        print("檢查號碼不正確，請重新輸入")
