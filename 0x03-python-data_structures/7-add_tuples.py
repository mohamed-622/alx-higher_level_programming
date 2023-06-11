def add_tuple(tuple_a=(), tuple_b=()):
    # Truncate the tuples to include only the first 2 integers
    tuple_a = tuple_a[:2]
    tuple_b = tuple_b[:2]

    # Pad the tuples with zeros if they are smaller than 2 elements
    tuple_a = tuple_a + (0, 0) if len(tuple_a) < 2 else tuple_a
    tuple_b = tuple_b + (0, 0) if len(tuple_b) < 2 else tuple_b

    # Compute the addition of the elements
    sum_1 = tuple_a[0] + tuple_b[0]
    sum_2 = tuple_a[1] + tuple_b[1]

    # Return the resulting tuple
    return sum_1, sum_2
