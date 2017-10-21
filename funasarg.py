st=raw_input("enter the string")
n=int(input("enter the number"))
def Exploder(string,n):
    print string * n

def Myfun(string,exploder,n):
    exploder(string,n)

Myfun(st,Exploder,n)