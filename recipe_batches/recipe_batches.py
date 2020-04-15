
import math

def recipe_batches(recipe, ingredients):
  batches={}
  max_batches = 10000

  for i in recipe:
    try:
      #floor devision!!!! WOW THIS TOOK ME WAY TOO LONG TO FIND!!!
      batches[i] = ingredients[i] // recipe[i]
    except:
      max_batches = 0
    
    for i in batches.values():
      if i < max_batches:
        max_batches = i
  
  return max_batches
    


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))