# Assignment 06, Task 05
# Name: Natthapee Sriarunluck
# Collaborators: -
# Time Spent: 01:00 hrs

calories = {"carb": 4, "protein": 4, "fat": 9}


def mealCal(meal: list[str], recipes: list[str], db: list[str]) -> float:
    dic_meal = {}
    dic_calories_ingredient = {}
    dic_calories_meal = {}
    # get dictionary of meal and frequency
    for i in meal:
        dic_meal[i] = dic_meal.get(i, 0) + 1
    # get dictionary of ingredient with total calories
    for i in db: 
        name, value = i.split(":")
        nutrients = value.split(",")
        total_cal = float(nutrients[0]) * 4 + float(nutrients[1]) * 4 + float(nutrients[2]) * 9
        dic_calories_ingredient[name] = total_cal
    # find total calories of each meal
    for i in recipes:
        name, recipe = i.split(":")
        ingredients = recipe.split(",")
        total_cal = 0
        for j in ingredients:
            x, y = j.split('*')
            total_cal += float(dic_calories_ingredient[x]) * float(y)
        dic_calories_meal[name] = total_cal
    # final calories on number of meals
    final_calories = 0
    for i in dic_meal:
        final_calories += float(dic_calories_meal[i]) * float(dic_meal[i])
    return final_calories


assert (mealCal(["T-Bone", "T-Bone", "Green Salad1"],
                ["Pork Stew:Cabbage*5,Carrot*1,Fatty Pork*10",
                 "Green Salad1:Cabbage*10,Carrot*2,Pineapple*5",
                 "T-Bone:Carrot*2,Steak Meat*1"],
                ["Cabbage:4,2,0", "Carrot:9,1,5", "Fatty Pork:431,1,5",
                 "Pineapple:7,1,0", "Steak Meat:5,20,10", "Rabbit Meat:7,2,20"]
                )) == 1290.0
