from operator import itemgetter



PEOPLE = [('Donald', 'Trump', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]

def format_sort_records(list):
    
    y=[]
   
    for i in list:
        y.append("{1:10} {0:10} {2:5.2f}".format(*i))

    y='\n'.join(y)
    return y


print(format_sort_records(PEOPLE))

