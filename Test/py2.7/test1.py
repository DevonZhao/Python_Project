# realize a function
def test(a,b,func):
    result = func(a,b)
    print(result)

func_new = input("please input a funciton:")
print type(func_new)
# func_new = eval(func_new)
test(2,3,func_new)



