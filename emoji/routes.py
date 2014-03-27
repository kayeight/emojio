from flask import render_template, request, session, url_for, redirect

import random

from emoji import app
from models import Emoji
from models import db

@app.route('/emoji/create/', methods=['POST'])
def create_emoji():
    emoji = Emoji(request.form.get('text'), int(request.form.get('category_id')))
    db.session.add(emoji)
    db.session.commit()

    return emoji.text

@app.route('/emoji/', methods=['GET'])
def random_emoji():
    all_emoji = Emoji.query.all()
    if len(all_emoji):
        return random.sample(all_emoji, 1)[0].text
    else:
        return ''

@app.route('/emoji/<int:emoji_id>', methods=['GET', 'PUT', 'DELETE'])
def get_emoji_by_id(emoji_id):
    text = request.args.get('text', None)

    emoji = Emoji.query.get_or_404(emoji_id)

    if request.method == 'PUT':
        if not text:
            return 'Text is required'
        # update emoji!!
        # db.session.commit()
        return emoji.text
    elif request.method == 'DELETE':
        db.session.delete(emoji)
        db.session.commit()
    else:
        return emoji.text