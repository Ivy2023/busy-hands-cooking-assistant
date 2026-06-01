"""
recipes_data.py

Application-specific data model and business logic for the
'Cooking Assistant' web app.

This module contains:
- A structured recipe data model
- Input parsing and validation
- Recipe matching logic

All code in this file is written specifically for this application.
"""

from typing import List, Dict, Set


# ---------------------------------------------------------------------------
# DATA MODEL
# ---------------------------------------------------------------------------

RECIPES: List[Dict[str, object]] = [
    {
        "name": "Simple Tomato Pasta",
        "ingredients": {
            "pasta": "200g",
            "tomato": "2 medium",
            "olive oil": "2 tbsp",
            "garlic": "2 cloves",
            "salt": "to taste",
        },
        "instructions": (
            "Boil pasta. Sauté garlic in olive oil, add tomato, cook until soft. "
            "Mix with pasta and season."
        ),
        "difficulty": "Easy",
    },
    {
        "name": "Vegetable Omelette",
        "ingredients": {
            "eggs": "3",
            "onion": "1/4 chopped",
            "tomato": "1 small",
            "cheese": "30g",
            "salt": "to taste",
            "pepper": "to taste",
        },
        "instructions": (
            "Beat eggs with salt and pepper. Add chopped vegetables and cheese. "
            "Cook in a pan until set."
        ),
        "difficulty": "Easy",
    },
    {
        "name": "Garlic Fried Rice",
        "ingredients": {
            "rice": "2 cups cooked",
            "garlic": "3 cloves",
            "oil": "1 tbsp",
            "soy sauce": "1 tbsp",
            "spring onion": "2 stalks",
        },
        "instructions": (
            "Fry garlic in oil. Add cooked rice and soy sauce. Stir-fry and "
            "finish with spring onion."
        ),
        "difficulty": "Medium",
    },
    {
        "name": "Chicken Stir Fry",
        "ingredients": {
            "chicken": "200g",
            "soy sauce": "2 tbsp",
            "garlic": "2 cloves",
            "ginger": "1 tsp grated",
            "vegetables": "1 cup mixed",
            "oil": "1 tbsp",
        },
        "instructions": (
            "Marinate chicken in soy sauce, garlic and ginger. Stir-fry with "
            "vegetables until cooked."
        ),
        "difficulty": "Medium",
    },
    {
        "name": "Creamy Mushroom Soup",
        "ingredients": {
            "mushroom": "200g",
            "cream": "200ml",
            "onion": "1 small",
            "garlic": "2 cloves",
            "butter": "1 tbsp",
            "salt": "to taste",
            "pepper": "to taste",
        },
        "instructions": (
            "Sauté onion and garlic in butter. Add mushrooms and cook. Pour in "
            "cream, simmer, blend until smooth."
        ),
        "difficulty": "Medium",
    },
    {
        "name": "Beef Tacos",
        "ingredients": {
            "beef": "200g",
            "tortilla": "4 pieces",
            "onion": "1/4 chopped",
            "tomato": "1 small",
            "lettuce": "1 cup shredded",
            "cheese": "40g",
            "spices": "1 tbsp",
        },
        "instructions": (
            "Cook beef with spices. Fill tortillas with beef, vegetables and "
            "cheese."
        ),
        "difficulty": "Easy",
    },
    {
        "name": "Pan-Seared Salmon",
        "ingredients": {
            "salmon": "1 fillet (150g_200g)",
            "lemon": "1/2",
            "salt": "to taste",
            "pepper": "to taste",
            "butter": "1 tbsp",
        },
        "instructions": (
            "Season salmon. Sear in butter until golden. Finish with lemon."
        ),
        "difficulty": "Easy",
    },
    {
        "name": "Vegetable Curry",
        "ingredients": {
            "potato": "1 medium",
            "carrot": "1 medium",
            "onion": "1 small",
            "garlic": "2 cloves",
            "ginger": "1 tsp grated",
            "curry paste": "1 tbsp",
            "coconut milk": "200ml",
        },
        "instructions": (
            "Sauté onion, garlic and ginger. Add curry paste, vegetables and "
            "coconut milk. Simmer until tender."
        ),
        "difficulty": "Medium",
    },
    {
        "name": "Homemade Pizza",
        "ingredients": {
            "flour": "250g",
            "yeast": "1 tsp",
            "water": "150ml",
            "tomato sauce": "4 tbsp",
            "cheese": "80g",
            "toppings": "as desired",
        },
        "instructions": (
            "Make dough with flour, yeast and water. Add sauce, cheese and "
            "toppings. Bake until golden."
        ),
        "difficulty": "Hard",
    },
    {
        "name": "Chocolate Cake",
        "ingredients": {
            "flour": "200g",
            "sugar": "150g",
            "cocoa": "50g",
            "eggs": "2",
            "butter": "100g",
            "milk": "150ml",
            "baking powder": "1 tsp",
        },
        "instructions": (
            "Mix dry ingredients. Add eggs, butter and milk. Bake until cooked "
            "through."
        ),
        "difficulty": "Hard",
    },
]

# ---------------------------------------------------------------------------


def normalise_ingredient(raw: str) -> str:
    """
    Normalise a single ingredient string:
    - Lowercase
    - Strip whitespace
    """
    return raw.strip().lower()


def parse_ingredients(raw_input: str) -> List[str]:
    """
    Convert a comma-separated string of ingredients into a clean list.

    Raises:
        ValueError: if the input is empty or contains no valid ingredients.
    """
    if not raw_input or not raw_input.strip():
        raise ValueError("No ingredients provided.")

    parts = [normalise_ingredient(p) for p in raw_input.split(",")]
    ingredients = [p for p in parts if p]

    if not ingredients:
        raise ValueError("No valid ingredients found in the input.")

    return ingredients


def find_matching_recipes(user_ingredients: List[str]) -> List[Dict[str, object]]:
    """
    Find recipes that match at least one of the user's ingredients.

    Matching logic:
    - Convert user ingredients to a set.
    - A recipe matches if it shares ≥1 ingredient.
    - Sort results by number of matching ingredients (descending).
    """
    user_set: Set[str] = {normalise_ingredient(i) for i in user_ingredients}

    results: List[Dict[str, object]] = []

    for recipe in RECIPES:
        recipe_ingredients = {
            normalise_ingredient(i) for i in recipe["ingredients"].keys()
        }
        matches = user_set.intersection(recipe_ingredients)

        if matches:
            recipe_copy = dict(recipe)
            recipe_copy["match_count"] = len(matches)
            recipe_copy["matched_ingredients"] = sorted(matches)
            results.append(recipe_copy)

    results.sort(key=lambda r: r["match_count"], reverse=True)
    return results
