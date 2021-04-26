def convertDecimalToBinary(number):
    temp = bin(number)[2:].zfill(4)
   
    return temp

print(convertDecimalToBinary(17))