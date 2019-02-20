##Write a function named count_char_x that takes a string named word and a single character named x as parameters. The function should return the number of times x appears in word.

# Write your count_char_x function here:
def count_char_x(word,x):
  number_of_appears = 0
  for i in word:
    if i == x:
      number_of_appears+=1
  return  number_of_appears

# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1