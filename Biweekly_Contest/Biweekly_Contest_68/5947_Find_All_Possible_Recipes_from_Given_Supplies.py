class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        recipes_dict = dict.fromkeys(recipes, False)
        recipes_dict_keys = recipes_dict.keys()
        supplies_dict = dict.fromkeys(supplies, True)
        supplies_dict_keys = supplies_dict.keys()
        ready_recipes = []
        length_of_recipes = len(recipes)

        for times in range(0, length_of_recipes):
            for index, ingredient in enumerate(ingredients):
                if (recipes_dict[recipes[index]] == True):
                    continue
                is_Ready = True
                for element in ingredient:
                    if (element not in supplies_dict_keys) and ((element not in recipes_dict_keys) or (recipes_dict[element] == False)):
                        is_Ready = False
                        break
                if (is_Ready == True):
                    recipes_dict[recipes[index]] = True

        for recipe in recipes_dict_keys:
            if (recipes_dict[recipe] == True):
                ready_recipes.append(recipe)

        return ready_recipes


