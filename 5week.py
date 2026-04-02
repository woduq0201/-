for i in range(2,9):
    print("# ", i ,"단  #  ",end="")
print("# 9단 #")
for num1 in range(1,10):
    for num2 in range(2,10):
        print(num2,"X",num1,"=",num2*num1,"  ",end="")
    print(num2,"X",num1,"=",num2*(num1))