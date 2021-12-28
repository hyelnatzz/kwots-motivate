from . import api_bp
from flask import current_app
from flask_restful import Resource, Api
from ..models import Quote

api = Api(api_bp)


class QuoteApi(Resource):
    def get(self, quote_id):
        quote = Quote.query.filter_by(id = quote_id).first()
        if quote == None:
            return {'message':'quote note found'}
        print(quote)
        return {'message':'success', 
                'author': quote.author, 
                'quote':quote.quote, 
                'categgory':quote.category.name,
                'category_color': quote.category.color.name,
                'date_created':quote.period}
        #return {'message': 'success'}


api.add_resource(QuoteApi, '/quote/<int:quote_id>/')



