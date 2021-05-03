import statistics
# list1 = [1, 2, 3, 4, 5]

def average(lst):
  # try:
    print("the average of your list is: ", statistics.mean(lst))
    return statistics.mean(lst)
  # except statistics.StatisticsError:
  #   raise Exception("let's see if this works")

# average(list1)