""" Implementation of Greedy Algorithm to solve 0/1 Knapsack Problems"""

class Item:
  def __init__(self, name, value, cost):
    self.name = name
    self.value = value
    self.cost = cost
  
  def __repr__(self):
    return f'<Item {self.name}>'
  
  def getDensity(self):
    return self.value / self.cost




def greedy(items:list, constraint, key_func):
  """ Solves 0/1 Knapsack Problem via "greedy" solution. I.E. Take the "best" available item until we reach our constraint.
      Returns a tuple (taken items, value of taken items, leftover budget)

      items: A list of Item instances to consider
      constraint: The total allowance of item cost allowed (e.g. size of the "knapsack")
      key_func: Sorting key function to define how we sort items from "best" to worst" (e.g. by value,  lowest cost or density)
  """
  results = []
  total_val, spent_cost = 0, 0
  # Begin by sorting our items from best to worst
  items_sorted = sorted(items, key=key_func, reverse=True)

  # Now simply iterate over our sorted list
  for i in range(len(items_sorted)):
    current = items_sorted[i]
    if (current.cost + spent_cost <= constraint):
      total_val += current.value
      spent_cost += current.cost
      results.append(current)
  
  return ( results, total_val, (constraint-spent_cost) )