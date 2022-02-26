from beer_catalog import BeerCatalog
from hela import generate_webpage


# Generate webpage and store in folder gh_pages
generate_webpage(
    BeerCatalog, output_folder='gh_pages', overwrite_existing=True,
    include_samples=True, web_app_title='Beer Catalog'
)
