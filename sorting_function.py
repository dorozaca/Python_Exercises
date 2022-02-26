def run():
    friends=['James','Biri','Carlos','Chicho','Rogger']
    friends.sort()
    friends.sort(reverse=True)
    print(friends)

    planets=[('Saturn',123,458),('Jupyter',421315,34445),('Venus',45664,7487)]
    distance=lambda x:x[1]
    planets.sort(key=distance,reverse=True) #possible to use key and reverse, but sort modifies the original list
    print(planets)                          #that is why cannot be applied to tuples

    numbers=(5,7,9,8,4)         #To order a tuple or even a list
    print(sorted(numbers))      #we need to use 'sorted' method a 
                                #It will  return a new list, leaving the original as is.

    word='Diego'                #Aforementioned comment applies here
    order=sorted(word)
    print(order)


if __name__== '__main__':
    run()


#Important: lists = list_name.sort()   -> returns list
            #tuples = sorted(tuple)    -> returns list too
