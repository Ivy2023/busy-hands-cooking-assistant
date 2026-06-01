"""
main.py

Flask-based web application that suggests recipes based on ingredients
available at home.

External library used:
- Flask (https://flask.palletsprojects.com/)

All application-specific business logic and data are in recipes_data.py.
"""

from flask import Flask, render_template, request
from recipes_data import parse_ingredients, find_matching_recipes

# Create Flask application instance
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Main page: shows a form and, on POST, displays matching recipes.

    Handles:
    - Empty input
    - Invalid input (e.g. only commas)
    - Unexpected errors with user-friendly messages
    """
    error_message = None
    recipes = []
    raw_ingredients = ""

    if request.method == "POST":
        raw_ingredients = request.form.get("ingredients", "")

        try:
            # Parse and normalize user input
            ingredients_list = parse_ingredients(raw_ingredients)

            # Find recipes (now supports ingredient amounts)
            recipes = find_matching_recipes(ingredients_list)

            if not recipes:
                error_message = (
                    "No recipes found with those ingredients. "
                    "Try adding more common items like 'garlic', 'rice' or 'eggs'."
                )

        except ValueError as value_error:
            # Expected validation errors (empty or invalid input)
            error_message = str(value_error)

        except Exception:
            # Unexpected errors: keep message generic for user experience
            error_message = (
                "Something went wrong while searching for recipes. "
                "Please try again."
            )

    return render_template(
        "index.html",
        error_message=error_message,
        recipes=recipes,
        raw_ingredients=raw_ingredients,
    )


if __name__ == "__main__":
    # Debug mode is useful during development.
    # For deployment, set debug=False or use environment configuration.
    app.run(debug=True)
