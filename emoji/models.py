from flask.ext.sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()

class Emoji(db.Model):
	__tablename__ = 'emoji'
	emoji_id = db.Column(db.Integer, primary_key=True)
	category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'))
	text = db.Column(db.String(40))
	short_name = db.Column(db.String(100))
	description = db.Column(db.String(255))

	def __init__(self, text, category_id):
		self.text = text
		self.category_id = category_id

	def __repr__(self):
		return '<Emoji %s>' % self.text

class Category(db.Model):
    __tablename__ = 'category'
    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, name):
		self.name = name

    def __repr__(self):
		return '<Category %s>' % self.name