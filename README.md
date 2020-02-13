# nfactor-decomp
N-factor decomposition code implementing the Sun (1998) method.

## Usage:
Use two lists of length `n`: one for the start year, the other for end year.

```
decomposition(n, values_start, values_end)
```

This returns the value at the start (product of `values_start`), the value at the end (product of `values_end`) and a list of `n` values, which are the differences due to each factor. The sum of the differences is equal to the difference between the value at the end and the value at the start.

Make sure to import `numpy` and `itertools`:
```
import numpy as np
import itertools
```
