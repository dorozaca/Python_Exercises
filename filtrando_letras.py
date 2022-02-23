def run():
    countries=['Finland', 'Ireland', 'Denmark', 'Peru','Brazil']

    land_countries=list(map(lambda x:x.upper(),filter(lambda x:'land' in x,countries))) #como buscar letras dentro de palabras en Python
    print(land_countries)                                                               #solo retorna las palabras que son True a esa busqueda
if __name__== '__main__':
    run()

    #Otro ejemplo de filter: odd=list(filter(lambda x:x%2 != 0, my list)) El segundo term del lambda tiene que ser un Booleano