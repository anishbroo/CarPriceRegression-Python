'''2. Transfrom the elements of list and store each transformation in new list
      i. Square each elements
    ii. Multiply each elements with 10 '''
  
num=list(range(0,10))
print(num)

num_sq=[]
num_x_10=[]
for ele in num:
    num_sq.append(ele**2 )
    num_x_10.append(ele*10)
print(num_sq)
print(num_x_10)
    
