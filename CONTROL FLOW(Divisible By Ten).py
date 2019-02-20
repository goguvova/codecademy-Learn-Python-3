##Create a function called divisible_by_ten() that has one parameter named num.
##
##The function should return True if num is divisible by 10, and False otherwise. Consider how to use modulo (%) to check for divisibility.

# Write your large_power function here:
def large_power(base,exponent):
  if base**exponent > 5000:
    return True
  else:
    return False
  

# Uncomment these function calls to test your large_power function:
print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False