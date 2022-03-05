def mysum(*args):
    if not args:       #siempre empezar validando que haya argumentos porque necesitamos index 0 para asigar tipo dinamicamente
        return args

    container=args[0]  #esto asigna dinamicamente el tipo a la variable//TRUCAZO!!!!
    for i in args[1:]: #como us o args[0] para asignar type dinamicamente, args tiene que empezar en index1 para que no repita value at index0
        container+=i   #como ya tiene el tipo asignado solo consolida o suma dependiendo el tipo
    return container


def run():
    name1='diego'
    name2='totom'
    number1=[1,2,3]
    number2=[4,5,6]

    print(mysum(name1,name2))
    print(mysum(number1,number2))
    print(mysum(3,5,7))
    

if __name__=='__main__':
    run()