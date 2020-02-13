import numpy as np
import itertools

def decomposition(n, values_start, values_end):

    # Make sure lists are numpy arrays
    values_start = np.array(values_start)
    values_end = np.array(values_end)

    if len(values_start) != n or len(values_end) != n:
        raise Exception("Input lists are not of length {}".format(n))

    diffs = values_end - values_start

    all_indices = set(range(n))

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

                contribution_level = (1.0/level) * np.prod(values_start[indices_start]) * np.prod(diffs[indices_diff])

                effect[i] += contribution_level

    value_start = np.prod(values_start)
    value_end = np.prod(values_end)
    
    np.testing.assert_almost_equal(np.sum(effect), value_end - value_start)
    
    return {
        'value_start': np.prod(values_start),
        'value_end': np.prod(values_end),
        'individual_effects': effect
    }




