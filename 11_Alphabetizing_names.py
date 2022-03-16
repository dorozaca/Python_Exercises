from operator import itemgetter


PEOPLE =[
{'first':'Reuven', 'last':'Lerner',
    'email':'reuven@lerner.co.il'},
 {'first':'Donald', 'last':'Trump',
    'email':'president@whitehouse.gov'},
 {'first':'Vladimir', 'last':'Putin',
    'email':'president@kremvax.ru'},
 ]


def alphabetize_names(mylist):
    #list2=sorted(mylist, key=lambda i:(i['last'],i['first']))
    list2=sorted(mylist,key=itemgetter('last','first'))
    return list2

def iterating(list):
    
    list2=[]
    for i in list:
        list2.append(i['last'])
        list2.append(i['first']) #para iterar en dicts necesitamos poner el valor del "key" no se puede usar int indexes
    return list2

def iterating2(listado):
    container2=[]
    for i in listado:
        # for j in i:
        #     print(j,i[j])
        container=i.values()
        container2.append(container)
    return container2


print(alphabetize_names(PEOPLE))
#print(iterating(alphabetize_names(PEOPLE)))
#print(iterating2(alphabetize_names(PEOPLE)))