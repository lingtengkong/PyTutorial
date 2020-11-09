"""
This model contains sum of arrays
"""


def add_array(x: list, y: list) -> list:
    """
    Returns the element-wise sum of x, y

    Args:
        x: the first list to add
        y: the second list to add

    returns:
        list: the pairwise sum of ``x`` and ``y``

    Raises:
        ValueError: If the length of the lists ``x`` and ``y`` are different.

    Examples:
        >>> add_array([1,2,3], [2,3,4])
        [3, 5, 7]
    """

    if len(x) != len(y):
        raise ValueError("Both arrays must have the same length.")

    z = []
    for x_e, y_e in zip(x, y):
        z.append(x_e + y_e)
    return z
