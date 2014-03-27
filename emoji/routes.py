from flask import render_template, request, session, url_for, redirect

from emoji import app
from models import Emoji
from models import db
import helpers

@app.route('/emoji/', methods=['GET', 'POST'])
def get_emoji():
    if request.method == 'POST':
        emoji = Emoji(request.form.get('text'), int(request.form.get('category_id')))
        db.session.add(emoji)
        db.session.commit()

        return emoji.text
    else:
        # return a random emoji!!
        pass

@app.route('/emoji/<int:emoji_id>', methods=['GET', 'PUT', 'DELETE'])
def get_emoji_by_id(emoji_id):
    emoji_id = helpers.ensure_int(emoji_id)
    emoji = Emoji.query.get(emoji_id)

    if request.method == 'PUT':
        # update emoji!!
        # db.session.commit()

        return repr(emoji)
    elif request.method == 'DELETE':
        db.session.delete(emoji)
        db.session.commit()
    else:
        return repr(emoji)