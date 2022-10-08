
def n():
    global num
    num=int(input("Enter Number of candidates: "))
    if 1<=num and num<=100:
        na()
    else:
        print("Enter Number beetwen 1-100")
        n()

def na():
    name = input("""Enter Nominator names: (separate with ",") """)
    l = name.split(",")
    if num==len(l):
        print(l)
        qad()
    else:
        print("tedad eshtebah ast")
        na()

def qad():
    q=input("""Enter Nominator hights: (separate with "|") """)
    if type(q)==str:
        l2 = q.split("|")
        if len(l2)==num:
            la=l2.copy()
        else:
            print("tedad eshtebah ast")
    else:
        print("Enter Number beetwen 1-300")
        qad()
    la = list(map(int, la))
    for i in range(len(la)):
        for j in range(i + 1, len(la)):

            if la[i] > la[j]:
                la[i], la[j] = la[j], la[i]
n()
