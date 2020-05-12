hashTable1 =[None,None,None,None,None,None,None,None,None,None,None,]
hashTable2 =[None,None,None,None,None,None,None,None,None,None,None,]

def hash1( key ):
    num = (key + 7)*(key + 7)
    num = num // 16
    num = num % 11
    return num

def hash2(key):
    jump = 1 + key // 11
    jump = jump % 10
    return jump

for i in [43,22,31,1,0,18,14,19,21]:
    hashPlace1 = hash1(i)
    hashPlace2 = hash2(i)
    print(hashPlace1)
    print(hashPlace2)
    if hashTable1[hashPlace1] == None:
        pass
    else:
        while hashTable1[hashPlace1] != None:
            hashPlace1+=1
    hashTable1.pop(hashPlace1)
    hashTable1.insert(hashPlace1,i)
    if hashTable2[hashPlace2] == None:
        pass
    else:
        while hashTable2[hashPlace2] != None:
            hashPlace2+=1
    hashTable2.pop(hashPlace2)
    hashTable2.insert(hashPlace2,i)
print(hashTable1)
print(hashTable2)