'''
Created on Jul 20, 2019

@author: vyomr
'''

'''
Swap values of two variables without using third variable 
'''
def swapVariables (var1, var2):
    print("----Swap values of two variables without using third variable ----")
    print('this is var1 : '+var1)
    print('this is var2 : '+var2)
    var1,var2 = var2,var1
    print('Swapped var1 : '+var1)
    print('Swapped var2 : '+var2)


'''
Let var = "HELLO" and print id of each character
'''
def printId (var):
    print("----Let var = \"HELLO\" and print id of each character----")
    for char in var:
        print("ID of "+char+" ="+str(id(char)))
        
'''
change the first character into upper case without using replace() function
'''
def changeFirstCharToUpperCase (var):
    print("----change the first character into upper case without using replace() function ----")
    print ("Input String is : "+var)
    varList = list(var)
    varList[0] = varList[0].upper()
    print ("Updated String is : "+"".join(varList))
    
def understandingDic():
    dictionaryVar = {'one':1,'two':2}
    print (dictionaryVar)
    print (dictionaryVar.get('three'))
    print (dictionaryVar['two'])
    '''
    print (dictionaryVar['three'])
    throws error, whereas dict.get(key) returns none when key is not available in dictionary
    '''
def main() : 
    a="test"
    b="swap"
    swapVariables(a,b)
    printId("HELLO")
    changeFirstCharToUpperCase("python")
    understandingDic()
    

main();
    
        
        