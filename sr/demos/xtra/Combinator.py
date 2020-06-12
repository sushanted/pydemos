
def combinator(*participants):
    indices = [0]*len(participants)
    while True:
        yield [participants[pindex][index] for pindex,index in enumerate(indices)]
        for i in reversed(range(len(indices))):
            indices[i]+=1
            if(indices[i]>=len(participants[i])):
                indices[i]=0
                if i==0: return
            else:
                break






def try1():

    for a,b,c,d,e in combinator(range(1,5),range(2,10),range(2,9),range(1,10),range(1,10)):
        #print((a,b,c,d,e,f,g,h,i))
        uniqueness=len(set((a, b, c, d, e)))
        #if (uniqueness ==5):
            #print((a, b, c, d, e))
        if(10*a+b) * c == 10*d+e and uniqueness==5  :
            print(f"{10*a+b}*{c}={10*d+e}")
            seen = set((a,b,c,d,e))
            #print(set(range(1,10))-seen)
            for f,g,h,i in combinator(
                    list(set(range(1,10))-seen),
                    list(set(range(1,10))-seen),
                    list(set(range(3,10))-seen),
                    list(set(range(1,10))-seen)
            ):
                if 10*d+e + 10*f+g == 10*h+i and len(set((f,g,h,i)))==4:
                    print(f"\t\t+{10*f+g}={10*h+i}")


try2()