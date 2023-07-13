from app import db


class Recipe(db.Model):
  id = db.Column(db.Integer(), primary_key=True)
  title = db.Column(db.String(),nullable=False)
  description = db.Column(db.String(),nullable=False)
  ingredient = db.Column(db.String(),nullable=False)
  preparation_instruction=db.Column(db.String(),nullable=False)

  def __repr__(self):
    return f"<Recipe {self.title}>"

  
  def save(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def update(self,title,description,ingredient,preparation_instruction):
    self.title=title
    self.description = description
    self.ingredient = ingredient
    self.preparation_instruction = preparation_instruction
    db.session.commit()



# user model
  # class User:
      # id:integer
      # username:string
      # email:string
      # password:string

class User(db.Model):
  id=db.Column(db.Integer(),primary_key=True)
  username=db.Column(db.String(25),nullable=False,unique=True)
  email=db.Column(db.String(80),nullable=False)
  password=db.Column(db.Text(),nullable=False)
  
  def __repr__(self):
    return f"<User {self.username}>"


  def save(self):
    db.session.add(self)
    db.session.commit()




    