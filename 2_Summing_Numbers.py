
#Exercise 2.a
#  def mysum(*numbers):
#     output=0
#     counter=0
#     for i in numbers:
#         output += i
#         counter +=1

#     print(output/counter)

# def run():
#     my_lucky_numbers=list(range(1,11))
#     mysum(*my_lucky_numbers)

# if __name__== '__main__':
#     run()


#Exercise 2.b

def string_analysis(*list):
    
    my_analysis=[]                                                     #since we are going to analyze string lengths, we are going to keep that info on this list                                                      
    for i in list:
        container=len(i)                                               #will iterate through the input list, get the length of each string element
        my_analysis.append(container)                                  #and add it to my_analysis which is now an int list

    counter = 0                                                         #Variable to count number of elements in my_analysis list
    sum=0                                                               #Variable to sum up lengths of each string element to calculate avg
    for i in my_analysis:
        sum +=i
        counter +=1
    average=(sum//counter)                                              #Using aforementioned variables to calculate average. Using // to take just integer part of result

    my_analysis.sort()                                                   #We can use sort to organize list by length. Another workaround to organize string lists by length is (key=len)
    return (my_analysis[0], my_analysis[len(my_analysis)-1], average)     #Display first element in list (index 0), the last element and average
                                                                          #Takes elements from list and returns a tuple: Sort of Conversion

        
def run():
    my_words=['cas','perro','Overland','Gonzalo','SilvioValencia']
    print(string_analysis(*my_words))                                      #Se tiene que usa splat (*) para desempaquetar la lista
                                                                           #se usa print para desplegar el return

if __name__== '__main__':
    run()                                                               #There is a more optimal solution with .sort(key=len). This function will
                                                                       #provide us with shortest and longest string automatically. Then we would only need 
                                                                       #a for loop to sum up lengths of each string and divide it by the result of len(List)
                                                                       #without subtracting -1 (because we are not looking for las index this time)
                                                                       # and return those results within a tuple