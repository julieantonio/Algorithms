#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  if len(recipe) <= len(ingredients):
    batch_arr = []
    for key in recipe and ingredients:
      batches = ingredients[key]//recipe[key]
      batch_arr.append(batches)
      max_batches = batch_arr[0]
    for b in range(len(batch_arr)-1):
      if batch_arr[b] < max_batches:
        max_batches = batch_arr[b]
    return max_batches
  return 0

print(recipe_batches({ 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }, { 'milk': 1288, 'flour': 9, 'sugar': 95 }))

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))