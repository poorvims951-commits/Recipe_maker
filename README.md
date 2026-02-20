Recipe Maker 

Recipe Maker is a Django-based web application that allows users to browse, view, and manage recipes in a stylish and professional interface. Users can see recipe images, descriptions, ingredients, and step-by-step instructions.



Features

- Home page with a welcome message.
- Browse a list of dishes with images and descriptions.
- View detailed recipe steps and ingredients.
- Separate navigation tabs for Ingredients and Steps.
- Admin interface to add, update, and delete recipes.
- Image upload support for recipes.
- Clean, professional, and responsive design.




Home Page 
![Home Page](screenshots/home.png)

Recipes List
![Recipes List](screenshots/recipes_list.png)

Recipe Details
![Recipe Details](screenshots/recipe_detail.png)



 Installation

1. Clone the repository:

git clone https://github.com/yourusername/recipe_maker.git
cd recipe_maker
Create and activate a virtual environment:

Windows
python -m venv env
env\Scripts\activate

macOS/Linux
python3 -m venv env
source env/bin/activate
Install dependencies:

pip install -r requirements.txt
If requirements.txt does not exist, install Django manually:

pip install django
Apply migrations:

python manage.py makemigrations
python manage.py migrate
Create a superuser (optional, for admin access):

python manage.py createsuperuser
Run the development server:

python manage.py runserver
Open your browser and go to:

http://127.0.0.1:8000/
Usage
Navigate through the home page and click View Dishes to see all recipes.

Click View Recipe on any dish to see detailed steps and ingredients.

Use the navigation tabs in the recipe detail page to view Ingredients or Steps separately.

Use the Django admin panel (/admin) to add, edit, or delete recipes.

Tech Stack
Backend: Django 6.0

Frontend: HTML, CSS, Bootstrap (optional for styling)

Database: SQLite (default Django database)

Python Version: 3.13
