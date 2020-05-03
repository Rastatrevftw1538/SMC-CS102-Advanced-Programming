def skipsearch(mylist, target, skip):
    for i in mylist[0:-1:skip]:
        print(i,"i")
        if i > target:
            for x in mylist[i:0:-1]:
                print(x,"x")
                if x == target:
                    return True
                elif x < target:
                    return False
        elif i == target:
            return True
    for x in mylist[-1:0:-1]:
            print(x,"x")
            if x == target:
                return True
            elif x < target:
                return False
    return False

def bigO():
    
def main():
    print(skipsearch([1,8,17,63,64,90,107,108],90,4))

main()