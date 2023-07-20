# tarsiers
Powerful Polars is Terser with Tarsiers

Tarsiers is an add-on to Polars enabling more concise expressions and
less typing. It is _primarily_ intended for interactive use where
quick iteration and concise code are most valuable.

More symbol-like columns, as it should be! For simply named columns
you can write `C.foo` instead of `pl.col("foo")`.

Symbol-like symbols. Only `N` for now, but it's a nice feature from
`data.table` to borrow.

```python

>>> import polars as pl
>>> import tarsiers as tr
>>> import tarsiers.col as C
>>> import tarsiers.symbols as S
>>> df = pl.DataFrame({"foo": [1, 3, 4], "bar": [3, 4, 0]})
>>> df.with_columns(
...     tr.cases(C.foo > 2, 1, C.bar > 2, 4, default = -1).alias("val")
... )
shape: (3, 3)
┌─────┬─────┬─────┐
│ foo ┆ bar ┆ val │
│ --- ┆ --- ┆ --- │
│ i64 ┆ i64 ┆ i32 │
╞═════╪═════╪═════╡
│ 1   ┆ 3   ┆ 4   │
│ 3   ┆ 4   ┆ 1   │
│ 4   ┆ 0   ┆ 1   │
└─────┴─────┴─────┘

>>> df.groupby(C.foo % 2 == 1).agg(S.N, C.bar.sum())
shape: (2, 3)
┌───────┬───────┬─────┐
│ foo   ┆ count ┆ bar │
│ ---   ┆ ---   ┆ --- │
│ bool  ┆ u32   ┆ i64 │
╞═══════╪═══════╪═════╡
│ false ┆ 1     ┆ 0   │
│ true  ┆ 2     ┆ 7   │
└───────┴───────┴─────┘

```