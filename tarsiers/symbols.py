import polars as pl
from polars import selectors as cs

N = pl.count()

I = cs.first().agg_groups().alias('idx')
