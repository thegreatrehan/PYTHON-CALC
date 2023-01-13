print("welcome to python calci")
print("select the operator by typing its symbol, make sure it is a valid operator or programm will exit automatically")

inp= input()

var1= "+"
var2= "-"
var3= "*"
var4= "/"


if var1==inp:
    print("opted for adittion")
    print("enter your first number")
    inp1= int(input())
    print("enter yur second number")
    inp2= int(input())
    print("result:")
    print(inp1 + inp2)
    print("code by REHAN.M.BAGEWADI")

elif var2==inp:
    print("you opted for substraction")
    print("enter your first number")
    inp3= int(input())
    print("enter your second number")
    inp4= int(input())
    print("result:")
    print(inp3 - inp4)
    print("code by REHAN.M.BAGEWADI")

elif var3 == inp:
    print("you opted for product")
    print("enter your first number")
    inp3 = int(input())
    print("enter your second number")
    inp4 = int(input())
    print("result:")
    print(inp3 * inp4)
    print("code by REHAN.M.BAGEWADI")

elif var4 == inp:
    print("you opted for division")
    print("enter your first number")
    inp3 = int(input())
    print("enter your second number")
    inp4 = int(input())
    print("result:")
    print(inp3 / inp4)
    print("code by REHAN.M.BAGEWADI")
    
else:
    print("no valid operator found, exiting....")
