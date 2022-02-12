# score = ((60 - (a+b+c+d+e)) * F + a*ps1 + b*ps2 + c*ps3 + d*ps4 + e*ps5)
# Objective:
#   Given values for F, ps1, ps2, ps3, ps4, ps5
#   Find values for a, b, c, d, e that maximize score
#
# Constraints:
#   Values for a, b, c, d, e can be either 10 or 0
#   a+b+c+d+e >= 20 (At least two must be 10)

# Shorthand:
#   BASELINE: The evaluation of (60 - (a+b+c+d+e))
#   ADDENDUM: The evaluation of (a*ps1 + b*ps2 + ... etc.)
#   TARGETS: a, b, c, d, e
#   MODIFIERS: ps1, ps2, ps3, ps4, ps5

# The problem: The more TARGETS we set to 10, the lower our BASELINE while the higher our ADDENDUM
# The value of F can shift the comparative value between BASELINE and ADDENDUM. When F is higher, BASELINE becomes more valuable.
# We must set at least two TARGETS to 10 in order to meet the constraint

# Greedy solution: Find how many TARGETS we can set to 10 before our ADDENDUM becomes less valuable than losses to our BASELINE * F.
# Call this number N. Then, we pick the highest N MODIFIERS and set their partner operand TARGETS to 10.
# If we ignore F (i.e. F = 1), then this ruleset is very simple. Any MODIFIER > 1 will be a net benefit to our score if its
# corresponding target is activated (set to 10).
# Could the association be, if MODIFIER > F, then activate that MODIFIER? It seems to be.
# Ergo, final greedy solution:
# Activate all MODIFIERS > F by setting their partner TARGET to 10
# If we sum(TARGETS) < 20, continue with highest MODIFIERS until sum(TARGETS) == 20

# Programatically, sort MODIFIERS from highest to lowest
# Keep a count of how many we've activated
# Iterate through sorted MODIFIERS
# If current MODIFIER > F, activate it
# If current MODIFIER <= F and count < 2, activate it
# Otherwise, break out of loop (everything else is set to zero as our constraint is met and further MODIFIERS would only reduce score if activated)

def greedy(F, psn:list):
  """ Assuming F is a number, psn is a list of 5 numbers """
  activations = { psn[0] : False, psn[1] : False, psn[2] : False, psn[3] : False, psn[4] : False }
  sortedPSN = sorted(psn, reverse=True)
  activated = 0
  addendum = 0
  for n in sortedPSN:
    if n > F or activated < 2:
      activations[n] = True
      activated += 1
      addendum += (n * 10)
    else:
      break
  
  # Calculate final score
  score = (60 - (activated * 10)) * F + addendum

  return (score, activations)

# Rather than sort, keep track of two highest ps# while we iterate through psn, using these to fulfill sum >= 20 constraint
# This allows us to solve in O(n) time at the cost of a little more memory
def fastGreedy(F, psn:list):
  """ Assuming psn is a list of 5 positive numbers """
  activations = { psn[0] : False, psn[1] : False, psn[2] : False, psn[3] : False, psn[4] : False }
  activated = 0
  addendum = 0
  # Store the highest n below F in index 1, and 2nd-highest n in index 0
  # This allows us to easily use our # of activations as a loop condition and index
  high = [-1, -1]
  for n in psn:
    if n > F:
      activations[n] = True
      activated += 1
      addendum += (n * 10)
    else:
      if n > high[1]:
        high[0] = high[1]
        high[1] = n
      elif n > high[0]:
        high[0] = n
  
  # Fulfill sum >= 20 constraint
  while activated < 2:
    n = high[activated]
    activations[n] = True
    activated += 1
    addendum += (n * 10)
  
  # Calculate final score
  score = (60 - (activated * 10)) * F + addendum

  return (score, activations)


# Brute-force solution: Examine all possible combinations of TARGETS being 0 or 10, and pick the scenario which results in the highest score
# We could implement this with a search tree, but would it beat the above ruleset? Certainly not in runtime performance.

from random import random

def test():
  F, psn = random(), [random(), random(), random(), random(), random()]
  score, activ = fastGreedy(F, psn)
  print("F:", F)
  print("psn:", psn)
  print("Score:", score)
  print("Activations:", activ)

test()