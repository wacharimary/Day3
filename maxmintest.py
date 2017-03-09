def find_max_min (a):
  
  if type(a)==list:
  
    maximum=max(a)
    minimum=min(a)
   
    if maximum==minimum:
        b=len(a)
        return [b]
    else:
       print([minimum,maximum])
      
  else:
    pass
find_max_min([1,2,3,4])
find_max_min([4, 4, 4, 4])
find_max_min([6,4])
find_max_min([4,66,6,44,7,78,8,68,2])
find_max_min([1,2,3,4])

