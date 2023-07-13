from flask_restx import Namespace,Resource,fields
from app.models import Recipe
from flask_jwt_extended import jwt_required
from flask import request



recipe_ns=Namespace("recipe",description="Namespace for recipes")

#model (serializer)
recipe_model=recipe_ns.model(
    "Recipe",
    {
      "id":fields.Integer(),
      "title":fields.String(),
      "description":fields.String(),
      "ingredient":fields.String(),
      "preparation_instruction":fields.String()
    }
)

@recipe_ns.route('/hello')
class HelloResource(Resource):
  def get(self):
    return {"message":"Hello World"}




@recipe_ns.route('/recipes')
class RecipesResource(Resource):
  # @jwt_required()
  @recipe_ns.marshal_list_with(recipe_model)
  def get(self):
    """Get all recipes"""
    recipes=Recipe.query.all()

    return recipes
  
  @recipe_ns.marshal_with(recipe_model)
  @recipe_ns.expect(recipe_model)
  @jwt_required()
  def post(self):
    """create New recipe"""

    data=request.get_json()

    new_recipe=Recipe(
      title=data.get('title'),
      description=data.get('description'),
      ingredient=data.get('ingredient'),
      preparation_instruction=data.get('preparation_instruction')
    )

    new_recipe.save()

    return new_recipe,201

@recipe_ns.route('/recipe/<int:id>')
class RecipeResource(Resource):

  @recipe_ns.marshal_with(recipe_model)
  # @jwt_required()
  def get(self,id):
    """Get recipe by id"""
    recipe=Recipe.query.get_or_404(id)

    return recipe, 200

  @recipe_ns.marshal_with(recipe_model)
  @recipe_ns.expect(recipe_model)
  @jwt_required()
  def put(self,id):
    """Update recipe by id"""

    recipe_to_update=Recipe.query.get_or_404(id)

    data=request.get_json()

    recipe_to_update.update(data.get('title'),data.get('description'),data.get('ingredient'),data.get('preparation_instruction') )

    return recipe_to_update,200

  @recipe_ns.marshal_with(recipe_model)
  def delete(self,id):
    """Delete recipe by id"""

    recipe_to_delete=Recipe.query.get_or_404(id)

    recipe_to_delete.delete()

    return recipe_to_delete
