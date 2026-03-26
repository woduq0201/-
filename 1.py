a = str(input("입력 진수 결정(16/10/8/2): "))

if a == "16":
   b = int(input("값입력: "),16)
   print("16진수->",hex(b))
   print("10진수->",int(b))
   print("8진수->",oct(b))
   print("2진수->",bin(b))

if a == "10":
   b = int(input("값입력: "))
   print("16진수->",hex(b))
   print("10진수->",int(b))
   print("8진수->",oct(b))
   print("2진수->",bin(b))

if a == "8":
   b = int(input("값입력: "),8)
   print("16진수->",hex(b))
   print("10진수->",int(b))
   print("8진수->",oct(b))
   print("2진수->",bin(b))

if a == "2":
   b = int(input("값입력: "),2)
   print("16진수->",hex(b))
   print("10진수->",int(b))
   print("8진수->",oct(b))
   print("2진수->",bin(b))
   
hex(10) #16
int() #10
oct(10) #8
bin(2) #2진수
#python int num16