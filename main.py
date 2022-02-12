from common.item import Item
from lec1.greedy import greedy
from lec2.brute_search import maxVal, fastMaxVal
from lec2.fib import fib, fastFib

foods = [
  Item('Wine', 89, 123),
  Item('Beer', 90, 154),
  Item('Beer', 90, 154),
  Item('Pizza', 95, 258),
  Item('Burger', 100, 354),
  Item('Fries', 90, 365),
  Item('Soda', 79, 150),
  Item('Apple', 50, 95),
  Item('Donut', 10, 195)
] 

maxCalories = 750

def output_greedy():
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
  print(f'Items taken: {taken} \n')

def output_brute():
  print('--- Use brute force algorithm to find best solution ---')
  value, items = fastMaxVal(foods, maxCalories)
  budget = maxCalories
  for n in items:
    budget -= n.cost
  print(f"Total Value: {value} Budget Remaining: {budget}")
  print(f"Items taken: {items}\n")

def output_fib(count=120, fast=False):
  for i in range(count):
    n = fastFib(i) if fast else fib(i)
    print(f"Fib {i}: {n}")

# output_greedy()
# output_brute()
# output_fib(fast=True)