def exercise_time():
    
   data_points=[ ]
   container=0
   
   while True:
        container=(input('Enter 10 km run time: '))
        if container == "":
            print('<enter>' '\n')
            break
        else:
            data_points.append(container)
            
   return data_points
    
def crunching_numbers(list):
  
  
  total=0
  counter=0
  for i in list:
      float_i=float(i)
      total +=float_i
      counter +=1
      
  average=total/counter
  
  print(f"Average of {average} over {counter} runs")
  
  
def run():
    crunching_numbers(exercise_time())
    
    
if __name__== '__main__':
    run()