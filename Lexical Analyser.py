import sys

def TheMainWork(mString):
    newString = ""
    for i in mString:
        if(i == "+" or i == "-" or i=="*" or
           i == "/" or i == "=" or i == "(" or i== ")" ):
            newString = newString + " " + i + " "
        else:
            newString = newString + i
    
    return newString.split()


def CheckCharacters(variable):
    rangeCheck = range(48,58)
    rangeCheck2 = range(65,96)
    rangeCheck3 = range(92,123)
    
    for i in variable:
        checkIfCharacterIsOk = 0
        for r1 in rangeCheck:
            if(i == chr(r1)):
                checkIfCharacterIsOk+=1
        for r2 in rangeCheck2:
            if(i==chr(r2)):
                checkIfCharacterIsOk+=1
        for r3 in rangeCheck3:
            if(i==chr(r3)):
                checkIfCharacterIsOk+=1
        if(i == "+" or i == "-" or i=="*" or i == chr(9) or
           i == "/" or i == "=" or i == "(" or i== ")"  or i == " " or i == "."):
            checkIfCharacterIsOk+=1
        
        
        if(checkIfCharacterIsOk == 0):
            print("Unknown Charachter!")
            sys.exit("Unknown Charachter!")



variable = raw_input("please enter your ideal input: ")
variable = variable.strip()
CheckCharacters(variable)


variable = TheMainWork(variable)
for character in variable:
    print(character)



