def skipsearch(mylist, target, skip):
    for i in mylist[0:-1:skip]:
        print(i,"i")
        if i > target:
            for x in mylist[i:0:-1]:
                print(x,"x")
                if x == target:
                    return True
    return False
def main():
    print(skipsearch([1,2,3,4,5,6,7,8,9,10],4,3))

main()