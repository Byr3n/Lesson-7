x=5
if type (x) is (int):
    print("true")
else:
    print("false")
x=0.5
if type (x) is not float:
    print("true")
else:
    print("false")
x=20
y=20
if x is y:
    print("x is the same as y")
y=30
if x is not y:
    print("x is different from y")