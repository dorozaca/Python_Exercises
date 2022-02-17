def run():
    array=list(i for i in range(1,101))
    num=int(input('Por favor ingrese el numero: '))

    high=len(array)-1
    low=0
    mid=low+ (high-low)//2

    while low<=high:
        if num==array[mid]:
           print(f'El numero {num} esta en posicion {mid}' )
           break
        elif num>array[mid]:
            low=mid+1
            mid=low+(high-low)//2
        
        else:
            high=mid-1
            mid=low+(high-low)//2


    


if __name__== '__main__':
    run()