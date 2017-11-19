from db import db

class StockModel(db.Model):
  __tablename__ = 'stocks'

  id = db.Column(db.Integer, primary_key=True)
  symbol = db.Column(db.String(80))
  main_page = db.Column(db.String(100))
  close = db.Column(db.Float(precision=2))
  low = db.Column(db.Float(precision=2))
  high = db.Column(db.Float(precision=2))
  open = db.Column(db.Float(precision=2))
  date = db.Column(db.String(80))
  # name = db.Column(db.String(80))
  # price = db.Column(db.Float(precision=2))
  # exchange = db.Column(db.String(80))
  # marketCap = db.Column(db.String(80))
  # peRatio = db.Column(db.Float(precision=2))
  # dayLow = db.Column(db.Float(precision=2))
  # dayHigh = db.Column(db.Float(precision=2))
  # fiftyTwoWeekLow = db.Column(db.Float(precision=2))
  # fiftyTwoWeekHigh = db.Column(db.Float(precision=2))
  # fiftyDayAverage = db.Column(db.Float(precision=2))

  def __init__(self, stock_data):
    self.symbol = stock_data['symbol']
    self.main_page = stock_data['main_page']
    self.close = stock_data['close']
    self.low = stock_data['low']
    self.high = stock_data['high']
    self.open = stock_data['open']
    self.date = stock_data['date']

  def json(self):
    return {
      "symbol": self.symbol,
      "main_page": self.main_page,
      "close": self.close,
      "low": self.low,
      "high": self.high,
      "open": self.open,
      "date": self.date
    }

  @classmethod
  def find_by_name(cls, symbol):
  	return cls.query.filter_by(symbol=symbol).first()

  def save_to_db(self):
  	db.session.add(self)
  	db.session.commit()

  def delete_from_db(self):
  	db.session.delete(self)
  	db.session.commit()



