##Create a function named every_other_letter that takes a string named word as a parameter. The function should return a string containing every other letter in word.

# Write your every_other_letter function here:
def every_other_letter(word):
  string = []
  for i in range(len(word)):
    if i%2 == 0:
      string.append(word[i])
  return "".join(string)
  #return string
    

    

# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 