from app import create_app, db
from app.config import DevConfig
from app.models import Recipe, User


app = create_app(DevConfig)


@app.shell_context_processor
def make_shell_context():
  return {
    "db":db,
    "Recipe":Recipe,
    "User":User  
  }


if __name__ == '__main__':
  app.run()
