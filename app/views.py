from flask import render_template
from app import app_obj, db
from .models import Recipe

@app_obj.route('/home')
def home():
    recipes = Recipe.query.all()
    featured = Recipe.query.filter(Recipe.name=="Green Eggs & Ham").first()
    return render_template('home.html', title='Home', user='Law', featured=featured, recipes=recipes)