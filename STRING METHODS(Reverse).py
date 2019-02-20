##Write a function named reverse_string that has a string named word as a parameter. The function should return word in reverse.

# Write your reverse_string function here:
def reverse_string(word):
  empty =[]
  for i in range(len(word)):
    empty.append(word[-i-1])
  return "".join(empty)

# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
#print(reverse_string("Hello world!"))
# should print !dlrow olleH
#print(reverse_string(""))
# should print