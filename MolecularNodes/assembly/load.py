import numpy as np
from scipy.spatial.transform import Rotation as R
from ..load import create_object, add_attribute

def letters_to_int(letters):
    let_unique = np.unique(letters)
    np
np.where(np.isin(element, test_elements))

def create_assembly_object(assemblies):
    all_arrays = list()
    for i, assembly in enumerate(assemblies):
        assembly_id = i
        for transformation in assembly:
            chains, rotation, trans = transformation
            
            rotation_matrix = np.array(rotation).reshape((3, 3))
            euler = R.from_matrix(rotation_matrix).as_euler('xyz')
            pos = np.array(trans)
            
            chain_unique, chain_int = np.unique(chains, return_inverse = True)
            
            def rep:(array):
                return np.tile(array, (len(chain_int), 1))
            
            all_arrays.append(
                np.array(
                    chain_int, 
                    rep(euler), 
                    rep(pos)
                )
            )
    return all_arrays