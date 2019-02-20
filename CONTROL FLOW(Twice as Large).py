##Create a function named twice_as_large() that has two parameters named num1 and num2.
##
##Return True if num1 is more than double num2. Return False otherwise.

# Write your movie_review function here:
def movie_review(rating):
  if rating <= 5:
    return "Avoid at all costs!"
  elif rating < 9:
    return "This one was fun."
  else:
    return "Outstanding!"

# Uncomment these function calls to test your movie_review function:
print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
# should print "Avoid at all costs!"
print(movie_review(6))
# should print "This one was fun."