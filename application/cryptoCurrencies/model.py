from application import db, app

app.app_context().push()

class CryptoCurrency(db.Model):
    __tablename__ = "cryptoCurrencies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    inventor_name = db.Column(db.String(100), nullable=False)
    greatest_of_all_time_price = db.Column(db.String(100), nullable=False)
    launch_date = db.Column(db.String(100), nullable=False)

    def __init__(self, name, inventor_name, greatest_of_all_time_price, launch_date):
        self.name = name
        self.inventor_name = inventor_name
        self.greatest_of_all_time_price = greatest_of_all_time_price
        self.launch_date = launch_date

    def __repr__(self):
        return f"CryptoCurrency(id: {self.id}, name: {self.name})"
    
    @property
    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "inventor_name": self.inventor_name,
            "greatest_of_all_time_price": self.greatest_of_all_time_price,
            "launch_date": self.launch_date
        }