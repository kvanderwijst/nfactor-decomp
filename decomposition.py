import numpy as np
import itertools

def prod(lst):
    value = 1.0
    for x in lst:
        value *= x
    return value

def decomposition(n, values_start, values_end):
    
    if len(values_start) != n or len(values_end) != n:
        raise Exception("Input lists are not of length {}".format(n))
    
    try:
        diffs = [v_end - v_start for v_start, v_end in zip(values_start, values_end)]
    except:
        raise Exception("Cannot substract values_start and values_end.")
    
    all_indices = set(range(n))
    
    # Initialise with array of zeros
    effect = [0]*n
    
    # For each factor i:
    for i in range(n):
        
        # Remaining indices
        indices = all_indices - set([i])
        
        # For each level 1 to n (incl)
        for level in range(1,n+1):
            num_start = n - level

            # Iterate over all combinations of remaining indices of length "num_start"
            for indices_start in itertools.combinations(indices, num_start):
                # "indices_start" are all the indices for the x_i-terms
                # "indices_diff" are all the indices for the delta x_i terms,
                # so the remaining indices

                indices_start = list(indices_start) # Transform tuple to list
                indices_diff = list(all_indices - set(indices_start))
                
                selection_start = [values_start[i] for i in indices_start]
                selection_diff = [diffs[i] for i in indices_diff]
                contribution_level = (1.0/level) * prod(selection_start) * prod(selection_diff)

                effect[i] += contribution_level
    
    value_start = prod(values_start)
    value_end = prod(values_end)
    
    return {
        'value_start': prod(values_start),
        'value_end': prod(values_end),
        'individual_effects': effect
    }
