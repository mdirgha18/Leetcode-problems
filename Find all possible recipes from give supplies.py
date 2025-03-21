class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Convert the supplies list to a set for O(1) lookup
        supplies = set(supplies)

        # Create a dictionary where keys are recipe names and values are their required ingredient
        recipes = dict(zip(recipes, ingredients))

        # List to store the successfully made recipes
        made = []

        # Basically check if we can keep making new stuff
        # Add to new list of supplies and delete recipe

        while True: # Keep looping untill no new recipes can be made
            # Track whether we made progress in this iteration 
            new_recipe = False # Flag to track if any new recipe is made in this track 

            # Iterate over a copy of dictionary to avoid modifying it while iterating 
            for rcp, igs in [*recipes.items()]:
                # Check if all the ingredients required for this recipe are in available supplies 
                if not all(i in supplies for i in igs):
                    # cannot be made (with current supplies)
                    continue # Skip this recipe if any ingredient is missing 
                made.append(rcp) # Recipe can be made, so add it to the list of made recipes
                supplies.add(rcp) # Add this recipe to the supplies (since now we can use it as an ingredient)
                del recipes[rcp] # Remove the recipe from the dictionary since it has been processed
                new_recipe = True # Mark that a new recipe was successfully made in this iteration 

            # If no new recipe was made in this iteration, break the loop (no more progress possible)
            if not new_recipe: 
                break

        # Return the list of all successfully made recipes
        return made
        
