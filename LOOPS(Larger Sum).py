##Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.
##
##The function should return the list whose elements sum to the greater number. If the sum of the elements of each list are equal, return lst1.

#Write your function here
def larger_sum(lst1,lst2):
  total1=0
  total2=0
  for i in lst1:
    total1+=i
  for i in lst2:
    total2+=i
  if total2>total1:
    return lst2
  else:
    return lst1
    
    
  


#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))