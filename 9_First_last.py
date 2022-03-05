def fistlast(seq):
    return seq[:1]+seq[-1:]

def even_odd_sums(mytuple):
    even = mytuple[::2]
    odd =  mytuple[1::2]

    a=0
    b=0

    for i in even:
        a+=i
    for i in odd:
        b+=i

    return [a,b]

def plus_minus(dato):
    subtra=dato[::2]
    addi=dato[1::2]

    a=subtra[0]*2
    b=0

    for i in subtra:
        a-=i
    for i in addi:
        b+=i

    return a+b

def zip(mytuple, myword):
    
    superlist=[]
    x=len(mytuple)
    for i in range(x):
        container=(mytuple[i],myword[i])
        superlist.append(container)

    return superlist


    
  
def run():
    seq=input('Enter sequence: ')
    mytuple=(10,20,30,40,50,60)
    myword='abcdef'
    
    print(fistlast(seq))
    print(even_odd_sums(mytuple))
    print(plus_minus(mytuple))
    print(zip(mytuple,myword))

if __name__=='__main__': 
    run()