a=1
b=0
try:
    print(x)
    print(a/b)
except NameError:
    print("Variable xis not defined")
except:
    print("Something else went wrong")
