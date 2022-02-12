""" Implementation of Brute Force algorithm to solve a 0/1 Knapsack problem. O(2^n)"""


def maxVal(toConsider:list, avail):
  """ Assumes toConsider a list of Item instances, avail a budget of available Item cost
      Recursively performs a binary search tree operation on the list, where the left child is a scenario in which
      the current item being considered is taken, and the right child is a scenario in which it is NOT taken.
      Returns a tuple of the total value of a solution, and tuple of the items included in that solution.
  """

  if len(toConsider) < 1 or avail == 0:
    result = ( 0, () )
  elif toConsider[0].cost > avail:
    # If our current item to consider's cost goes beyond our budget, we can only explore the right
    # branch of our search tree (i.e. don't take the item)
    result = maxVal(toConsider[1:], avail)
  else:
    curItem = toConsider[0]

    # Recursively explore left branch...
    leftVal, leftTake = maxVal( toConsider[1:], avail - curItem.cost )
    # ...Then add the value of the current decision
    leftVal += curItem.value
    
    # Recursively explore right branch (do not choose curItem)
    rightVal, rightTake = maxVal( toConsider[1:], avail)

    # Choose the better branch
    result = (leftVal, leftTake + (curItem, )) if leftVal > rightVal else (rightVal, rightTake)

  return result