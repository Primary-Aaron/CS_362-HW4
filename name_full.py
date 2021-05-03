import random

def fullName(first, last):
  mNames = ["Bill", "Ted", "Jerry", "Michael", "Franklin", "Oliver"]
  return first + " " + mNames[int(random.randrange(len(mNames)))]+ " " +last
