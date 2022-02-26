from hela import Catalog
from beer_catalog.datasets.sales.orders import orders
from beer_catalog.datasets.sales.beer_info import beer_info
from beer_catalog.datasets.web.user_interactions import user_interactions
from beer_catalog.datasets.web.beer_reviews import beer_reviews


@Catalog.setup(rich_description_path='examples/rich_descriptions/beer_catalog.md')
class BeerCatalog(Catalog):

    @Catalog.setup(folder='showcase_data/sales', description='Collection of datasets related to sales.')
    class Sales(Catalog):
        orders = orders
        beer_info = beer_info

    @Catalog.setup(
        folder='showcase_data/web',
        description='Collection of datasets related to website and user interactions.'
    )
    class Web(Catalog):
        user_interactions = user_interactions
        beer_reviews = beer_reviews
