#Sals Shipping

def print_cheapest_shipping_method(weight):
  print("The cheapest option available is $%.2f with %s shipping")

def ground_ship(weight):
  if weight >= 10:
    cost = 4.75
  elif weight >= 6:
    cost = 4
  elif weight >= 2:
    cost = 3
  elif weight >= 0:
    cost = 1.50
  total_cost = weight * cost + 20
  print(total_cost)
  return(total_cost)  # have the function return the calculated value

premium_ship = 125

def drone_ship(weight):
  if weight >= 10:
    cost = 14.25
  elif weight >= 6:
    cost = 12
  elif weight >= 2:
    cost = 9
  elif weight >= 0:
    cost = 4.5
  total_cost = weight * cost
  print(total_cost)
  return(total_cost)  # have the function return the calculated value

ground_ship(10)
drone_ship(1.5)

def best_deal(weight):
  # now you can compare values, by calling each function with the given 'weight'
  if ground_ship(weight) < drone_ship(weight) and ground_ship(weight) < premium_ship:
    method = "standard ground"
    cost = ground_ship(weight)  # get the cost from the function calculation

  elif premium_ship < drone_ship(weight) and premium_ship < ground_ship(weight):
    method = "premium"
    cost = premium_ship  # in this case, premium_ship is a value
  else:
    method = "drone"
    cost = drone_ship(weight)  # get the cost from the function calculation

  print("The cheapest option for your package is " + method + " shipping and the cost will be $" + str(cost))

best_deal(10)