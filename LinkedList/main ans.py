from llist_ans_rev import Node
from llist_ans_rev import LinkList

def main():
    n = Node("two")
    print("n's data = ", n.getData())
    print("n's pointer =", n.getNext() )
    input()

    nl = LinkList()
    print(nl)
    nl.add(11)
    print(nl)
    print("building a linked list...")
    for i in range(3,15, 2):
        nl.add(i)
        print("current nl is", nl)
    print("final nl's size is", nl.size)
    print("final nl = ", nl)
    print("now we know 'add' works") 
    input()
    
    print("Is 9 in nl:", nl.search(9))
    print("Is 10 in nl:", nl.search(10))
    input()

    print("Which spot is 7 in:",nl.index(7))
    print("Which spot is 14 in:",nl.index(14))
    input()
    
    nl.insert(4, 88)
    print("Inserted 88 into 4th spot")
    print(nl)
    input()
    
    nl.remove(13)
    print("removed the 13 (old head)")
    print(nl)
    input()

    nl.remove(7)
    print("removed the 7")
    print(nl)
    input()

    nl.remove(22)
    print("removed the first 22")
    print(nl)
    input()

    nl.pop()
    print("popped off the end")
    print(nl)
    input()


    nl.mover()
    print(nl)
main()
