from strands import tool


@tool
def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b

@tool
def square(n: int) -> int:
    """Return n squared."""
    return n * n
