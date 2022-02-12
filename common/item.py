class Item:
  def __init__(self, name, value, cost):
    self.name = name
    self.value = value
    self.cost = cost
  
  def __repr__(self):
    return f'<Item {self.name}>'
  
  def getDensity(self):
    return self.value / self.cost