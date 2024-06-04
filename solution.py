

"""
INSTRUCTIONS:
DO NOT make changes to any code directly above a "your code here" comment.
ONLY add new lines after a "your code here" comment that creates, edits, or deletes the provided data.
"""


## create_meal
## define a variable named meal_1 that is a dictionary with properties of title, description, and cost
## that are a string, string, and float respectively

# your code here
meal_1 = { "title": "Spaghetti", "description": "Pasta with tomato sauce", "cost": 10.00 }


## update_meal
## using the meal_2 variable provided below, but without changing the original definition,
## change the cost to 12.00

meal_2 = { "title": "Spaghetti", "description": "Pasta with tomato sauce", "cost": 10.00 }
# your code here
meal_2['cost'] = 12.00


## delete_description
## using the meal_3 variable provided below, but without changing the original definition,
## remove the description key and value from the dictionary

meal_3 = { "title": "Spaghetti", "description": "Pasta with tomato sauce", "cost": 12.00 }
# your code here
del meal_3['description']


## get_title
## using the meal_4 variable provided below, create a new variable named title
## and get the value of the title from the meal_4 dictionary

meal_4 = { "title": "Spaghetti", "description": "Pasta with tomato sauce", "cost": 12.00 }
# your code here
title = meal_4['title']


## get_length
## using the meal_5 variable provided below, create a new variable named meal_length
## whose value is the number of keys in the meal_5 dictionary

meal_5 = { "title": "Spaghetti", "description": "Pasta with tomato sauce", "cost": 12.00 }
# your code here
meal_length = len(meal_5)


## update_meal
## using the meal_6 and meal_6_new variables provided below, merge meal_6_new into meal_6
## so that meal_6 contains all of the keys and values of meal_6_new

meal_6 = { "title": "Spaghetti", "description": "Pasta with tomato sauce", "cost": 12.00 }
meal_6_new = { "title": "Spicy Meatball Spaghetti", "description": "Pasta with some zing" }
# your code here
meal_6.update(meal_6_new)


## translate_meal
## using the meal_7 and translator variables provided below,
## loop over meal_7's title and add each english word to translated_meal_7
## if it is NOT the last word in the title, add a space to the end of translated_meal_7

meal_7 = { "title": ["Arroz", "con", "Pollo"], "description": "Que rico", "cost": 12.00 }
translator = { "Leche": "Milk", "Arroz": "Rice", "del": "of the", "Tigre": "Tiger", "con": "with",  "Pollo": "Chicken" }
translated_meal_7 = ""
# your code here
for word in meal_7['title']:
  translated_meal_7 += translator[word]
  if word != meal_7['title'][-1]:
    translated_meal_7 += " "


## count_keys
## using the meal_8 variable provided below,
## loop over meal_8 and increment key_count by one for each key in the dictionary

meal_8 = { "title": "Spaghetti", "description": "Pasta with tomato sauce", "cost": 12.00, "size": "Lg" }
key_count = 0
# your code here
for key in meal_8:
  key_count += 1




