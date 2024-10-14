from flask import Flask, jsonify, request
from db_utils import get_all_recipe_collection, get_breakfast_recipes, get_lunch_recipes, get_dinner_recipes, get_all_recipe_with_id, delete_recipe_by_id

app = Flask(__name__)

@app.route("/recipes", methods=["GET"])
def get_all_recipes():
    return jsonify(get_all_recipe_collection())

@app.route("/recipes/id", methods=["GET"])
def get_all_recipes_with_id():
    return jsonify(get_all_recipe_with_id())

@app.route("/recipes/breakfast", methods=["GET"])
def get_all_breakfast_recipes():
    return jsonify(get_breakfast_recipes())

@app.route("/recipes/lunch", methods=["GET"])
def get_all_lunch_recipes():
    return jsonify(get_lunch_recipes())

@app.route("/recipes/dinner", methods=["GET"])
def get_all_dinner_recipes():
    return jsonify(get_dinner_recipes())

@app.route("/recipes/remove/<int:id>", methods=["DELETE"])
def del_recipe_by_id(id):
    return jsonify(delete_recipe_by_id(id))


if __name__ == "__main__":
    app.run(debug=True)