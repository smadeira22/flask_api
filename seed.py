from application import db
from application.cryptoCurrencies.model import CryptoCurrency

db.drop_all()
print("Dropping Database")

db.create_all()
print("Creating Database")

print("Seeding Database")
entry1 = CryptoCurrency(name="Bitcoin", inventor_name ="Satoshi Nakamoto", greatest_of_all_time_price="$67.566", launch_date="3rd of January 2009")

entry2 = CryptoCurrency(name="Dogecoin", inventor_name="Billy Markus and Jackson Palmer", greatest_of_all_time_price="$0.74", launch_date="6th of December 2013")

entry3 = CryptoCurrency(name="SHIBA INU", inventor_name="Ryoshi", greatest_of_all_time_price="$0.00008845", launch_date="3rd of January 2020")

entry4 = CryptoCurrency(name="Solana", inventor_name="Anatoly Yakovenko", greatest_of_all_time_price="$258", launch_date="March 2020")

db.session.add(entry1)

db.session.add_all([entry2, entry3, entry4])

db.session.commit()