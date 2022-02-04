from greedy import Item, greedy

foods = [
  Item('Wine', 89, 123),
  Item('Beer', 90, 154),
  Item('Pizza', 95, 258),
  Item('Burger', 100, 354),
  Item('Fries', 90, 365),
  Item('Soda', 79, 150),
  Item('Apple', 50, 95),
  Item('Donut', 10, 195)
] 

maxCalories = 750

def output_results():
  print('--- Use greedy strategy, favoring highest item value ---')

  taken, val, budget = greedy(foods, maxCalories, lambda x : x.value)
  print(f'Total Value: {val} Budget Remaining: {budget}')
  print(f'Items taken: {taken} \n')

  print('--- Use greedy strategy, favoring lowest item cost ---')

  taken, val, budget = greedy(foods, maxCalories, lambda x : 1 / x.cost)
  print(f'Total Value: {val} Budget Remaining: {budget}')
  print(f'Items taken: {taken} \n')

  print('--- Use greedy strategy, favoring highest ratio of item value : cost --- ')

  taken, val, budget = greedy(foods, maxCalories, Item.getDensity)
  print(f'Total Value: {val} Budget Remaining: {budget}')
  print(f'Items taken: {taken}')

output_results()