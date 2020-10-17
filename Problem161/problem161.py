StrToTuple = lambda binaryString: tuple(x for x in binaryString)

def reverseBinary(bList: tuple):
    if (1 == len(bList)):
        if ('1' == bList[0]):
            return '0'
        return '1'
    if ('1' == bList[0]):
        return '0' + str(reverseBinary(bList[1:]))
    return '1'+str(reverseBinary(bList[1:]))

bStr = "11110000111100001111000011110000"
rbStr = reverseBinary(StrToTuple(bStr))
print(f"Given Binary numer: {bStr} \nReverse Binary Number: {rbStr} ")