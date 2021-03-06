from hela.datasets.pandas_parquet_dataset import PandasParquetDataset
from hela import Col, NestedCol
from hela.data_types import Int, Bool
from beer_catalog.column_store import ColumnStore


beer_reviews = PandasParquetDataset(
    name='beer_reviews',
    description='Collection of reviews of beer made by users on the website.',
    rich_description_path='beer_catalog/rich_descriptions/beer_reviews.md',
    partition_cols=['date'],
    columns=[
        ColumnStore.date,
        ColumnStore.timestamp,
        ColumnStore.user_id,
        ColumnStore.product_code,
        ColumnStore.product_name,
        ColumnStore.product_category,
        NestedCol('ratings', [
            Col('taste', Int(), 'A 1-5 rating of how well the beer tastes.'),
            Col('design', Int(), 'A 1-5 rating of how well designed the etiquette is.')
        ]),
        Col('is_guest', Bool(),
            'Whether the user leaving the review is logged in as guest or not.'),
    ]
)
