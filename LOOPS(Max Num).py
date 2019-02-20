##Create a function named max_num() that takes a list of numbers named nums as a parameter.
##
##The function should return the largest number in nums

#Write your function here
def max_num(nums):
  maxx = nums[0]
  for i in nums:
    if i >maxx:
      maxx =i
  return maxx
    


#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))