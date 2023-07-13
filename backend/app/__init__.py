from flask import Flask
from flask_restx import Api, Resource, fields
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


db=SQLAlchemy()
migrate=Migrate()
jwt_manager = JWTManager()
cors = CORS()
api=Api(doc='/docs')


def create_app(config):
  app=Flask(__name__)
  app.config.from_object(config)

  db.init_app(app)
  migrate.init_app(app, db, render_as_batch=True, compare_type=True)
  jwt_manager.init_app(app)
  cors.init_app(app)
  api.init_app(app)


  from app.recipes import recipe_ns
  from app.auth import auth_ns


  api.add_namespace(recipe_ns)
  api.add_namespace(auth_ns)

  return app
