import numpy as np

def reshape_array(data: list, operation: str) -> np.ndarray:
    """
    Returns a float64 array with the shape selected by operation.
    """
    da = np.array(data,dtype=float)
    if operation=="flatten":
        return da.flatten()
    if operation=="transpose":
        return da.T
    if operation=="add_batch":
        return np.expand_dims(da,axis=0)
        
        
    
