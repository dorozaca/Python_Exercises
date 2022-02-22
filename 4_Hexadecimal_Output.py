
def hex_output():
    decnum = 0
    hexnum = input('Enter a hex number to convert: ') #Probar con F7D = 3965
    for power, digit in enumerate(reversed(hexnum)):              
        decnum += int(digit, 16) * (16 ** power)         #Int puede tomar segundo argumento (16) para saber que estamos trabajando con hexa
    print(decnum)

def run():
    hex_output()   

if __name__== '__main__':
    run()

