def keywordFunctionTest(arg1,arg2,arg3):
    print(arg1)
    print(arg2)
    print(arg3)
    
def variableFunctionTest(variable1):
    variable1="test";
    print(variable1)

outVar1 = "real"
variableFunctionTest(outVar1)
print(outVar1)
    
    
keywordFunctionTest("Vyom", arg3="test", arg2=10)


def main():
    bar1='test'
    try: 
        print(bar1)
    except Exception as e:
        print('Error..........')
        print(e.with_traceback())
        
main() 