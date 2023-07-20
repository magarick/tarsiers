import polars as pl

def cases(*args, default=None):
    """
    Create a repeating when/then expression ending in anotherwise

    Parameters
    ----------
    *args
        Alternating conditions (when) and values (then). Naturally, you need an even number of these.
    default
        Value for otherwise
    """
    if len(args) == 0:
        raise pl.ShapeError("No cases provided")
    if len(args) % 2 != 0:
        raise pl.ShapeError(
            "Provide an even number of positional arguments consisting of alternating conditions and values"
        )
    expr = pl
    for i, a in enumerate(args):
        if i % 2 == 0:
            expr = expr.when(a)
        else:
            expr = expr.then(a)

    return expr.otherwise(default)
