# busy-hands-cooking-assistant
# Cooking Assistant – Ingredient-based Recipe Finder

## Overview

Cooking Assistant is a small Python web application that suggests recipes based on the ingredients you already have at home. You type a comma-separated list of ingredients, and the app returns recipes that use at least one of them, sorted by how many ingredients match.

This project demonstrates:

- A simple data model for recipes
- Web application logic using Flask
- Input validation and error handling
- Clear separation between application code and external libraries
- Basic manual testing and deployment guidance

---

## Features and value

- **Ingredient-based search:** Quickly discover what you can cook without browsing long recipe lists.
- **User-friendly feedback:** Helpful messages for empty or invalid input and when no recipes are found.
- **Readable codebase:** Well-structured modules, meaningful names and comments suitable for learning and maintenance.
- **Extensible data model:** New recipes can be added easily in `recipes_data.py`.

---

## Project structure

```text
cooking-assistant/
├── main.py            # Flask app, routes, and web flow
├── recipes_data.py   # Data model and business logic (application-specific)
└── templates/
    └── index.html    # HTML template for the web interface


## Web flow
app.py defines a single route / that accepts GET and POST.

On GET, it shows the form.

On POST, it:

Reads the ingredients field.

Uses parse_ingredients and find_matching_recipes.

Handles:

ValueError for validation issues (user-friendly message).

Generic Exception for unexpected errors (generic message).

This uses standard constructs: functions, selection (if/else), repetition (loops), data structures (lists, sets, dictionaries) and modules.

Error and input handling
Empty input or input with only commas triggers a ValueError in parse_ingredients.

The user sees a clear message such as:

“No ingredients provided.”

“No valid ingredients found in the input.”

Unexpected errors are caught in app.py and shown as:

“Something went wrong while searching for recipes. Please try again.”

This improves user experience and demonstrates exception handling.

Manual testing procedures
You can validate the code manually with the following tests:

Normal input:

Input: rice, garlic

Expected: At least one recipe (e.g. “Garlic Fried Rice”) is shown.

Multiple ingredients:

Input: eggs, tomato, cheese

Expected: “Vegetable Omelette” appears with matched ingredients listed.

Empty input:

Input: (leave the field empty and submit)

Expected: Error message “No ingredients provided.”

Only commas / spaces:

Input: , , ,

Expected: Error message “No valid ingredients found in the input.”

No matching recipes:

Input: chocolate, strawberries

Expected: Message that no recipes were found.

Unexpected error simulation (optional):

Temporarily raise an exception inside find_matching_recipes and confirm the generic error message appears.

Coding style and linting
The code follows PEP 8 style guidelines:

Meaningful variable and function names

Consistent indentation (4 spaces)

Line length kept reasonable

