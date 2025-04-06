from app import db
from app.models.quote import Quote

def create_quote(data):
    new_quote = Quote(author=data['author'], quote=data['quote'])
    db.session.add(new_quote)
    db.session.commit()
    return new_quote

def get_all_quotes():
    return Quote.query.all()

def get_quote_by_id(quote_id):
    return Quote.query.get(quote_id)

def update_quote(quote, data):
    quote.author = data.get('author', quote.author)
    quote.quote = data.get('quote', quote.quote)
    db.session.commit()
    return quote

def delete_quote(quote):
    db.session.delete(quote)
    db.session.commit()
