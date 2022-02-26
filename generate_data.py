import shutil
from pathlib import Path
from beer_catalog import BeerCatalog, _data_generators


# If the folder already exists, remove it first
p = Path('showcase_data')
if p.exists():
    shutil.rmtree(p)

# Make sales folder
(p / 'sales').mkdir(parents=True)
# Make web folder
(p / 'web').mkdir(parents=True)

# Generate and store data for demo purposes
BeerCatalog.Sales.beer_info.write(_data_generators.generate_beer_info_dataframe())
BeerCatalog.Sales.orders.write(_data_generators.generate_orders_dataframe())
BeerCatalog.Web.beer_reviews.write(_data_generators.generate_beer_reviews_dataframe())
BeerCatalog.Web.user_interactions.write(_data_generators.generate_user_interaction_dataframe())
