for i in range(2,9):
    print("# ", i ,"단  #  ",end="\t")
print("# 9단 #")
for num1 in range(1,10):
    for num2 in range(2,9):
        print(num2,"X",num1,"=",num2*num1,"  ",end="\t")
    print(num2+1,"X",num1,"=",(num2+1)*num1)