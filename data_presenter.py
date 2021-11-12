# Part 2
# 2.
open_file = open("CupcakeInvoices.csv")

# 3.
#for line in open_file:
#    print(line)

# 4.   
for line in open_file:
    type = line.split(',') 
    print(type[2])     
    
# 5.
total = 0

for line in open_file:
  data = line.split(',')
  total = int(data[3]) * float(data[4])
  print(total)
  
 # 6.
total = 0

for line in open_file:
  data = line.split(',')
  total = total + (int(data[3]) * float(data[4]))
  print(total)
  
# 7.
open_file.close()  
             
            
            
            
 
       
            
            
    
    