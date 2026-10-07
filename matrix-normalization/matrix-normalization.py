import numpy as np

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as matrix.
    """
    matrix = np.array(matrix, dtype=float)

    # Replace NaN with 0
    matrix = np.nan_to_num(matrix, nan=0.0)

    if norm_type == "l1":
        ord_value = 1
    elif norm_type == "l2":
        ord_value = 2
    elif norm_type == "max":
        ord_value = np.inf
    else:
        raise ValueError("Invalid norm_type")

    # Compute norm
    if axis is None:
        norm = np.linalg.norm(matrix.ravel(), ord=ord_value)
    else:
        norm = np.linalg.norm(
            matrix,
            ord=ord_value,
            axis=axis,
            keepdims=True
        )

    # Avoid division by zero
    return np.divide(
        matrix,
        norm,
        out=np.zeros_like(matrix),
        where=norm != 0
    )