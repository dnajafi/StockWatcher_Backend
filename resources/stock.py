from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.stock import StockModel
from stock_crawler import get_historical_data

class Stock(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('symbol',
		type=str,
		required=True,
		help="Symbol field cannot be left blank!"
	)

	@jwt_required()
	def post(self):
		data = Stock.parser.parse_args()
		if StockModel.find_by_name(data.symbol):
			return {"message": "A stock with the symbol '{}' already exists".format(data.symbol)}, 400

		stock_data = get_historical_data(data.symbol, 1)[0]
		stock = StockModel(stock_data)

		try:
			stock.save_to_db()
		except:
			return {"message": "An error occurred inserting the stock"}, 500

		return stock.json()


class StockList(Resource):
	# @jwt_required()
	def get(self):
		return {'stocks': [stock.json() for stock in StockModel.query.all()]}