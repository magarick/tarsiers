import polars as pl

def __getattr__(c):
    return pl.lit(c)
