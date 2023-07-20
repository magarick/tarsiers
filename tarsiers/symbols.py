import polars as pl

N = pl.count()

# Doesn't quite work yet. Don't want it to return one list per column
# and we shouldn't have to know column names ahead of time

#I = pl.all().agg_groups()
