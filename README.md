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
├── app.py            # Flask app, routes, and web flow
├── recipes_data.py   # Data model and business logic (application-specific)
└── templates/
    └── index.html    # HTML template for the web interface
