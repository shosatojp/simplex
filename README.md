# simplex-method

## Install

```sh
pip install simplex
```

## Usage

```py
import numpy as np
from simplex import simplex, rationals

# max = True, min = False
MAX = False
# 目的関数係数
c = np.array(rationals([0, 0, 0, 0, 0, 1, 1, 1]))
c_name = [f'x{i+1}' for i in range(len(c))]

# 制約条件係数行列
m = np.array(rationals([
    [1, 2, 1, 0, 0, 1, 0, 0, 20],
    [7, 6, 0, -1, 0, 0, 1, 0, 84],
    [1, -1, 0, 0, 1, 0, 0, 1, 8],
]))

# 基底変数
base_name = ['x6', 'x7', 'x8']
base = np.array([c[c_name.index(e)] for e in base_name])

simplex(MAX, c, c_name, m, base, base_name)
```

## Output

```
               c   0   0   0   0   0   1   1   1              
 base  base_name  x1  x2  x3  x4  x5  x6  x7  x8  const  theta
    1         x6   1   2   1   0   0   1   0   0     20     20
    1         x7   7   6   0  -1   0   0   1   0     84     12
    1         x8   1  -1   0   0   1   0   0   1      8      8
              pi   9   7   1  -1   1   1   1   1    112       
          c - pi  -9  -7  -1   1  -1   0   0   0              
pivot(col = x1, row = x8)
--------------------------------------------------------------------------------
               c   0    0   0   0   0   1   1   1              
 base  base_name  x1   x2  x3  x4  x5  x6  x7  x8  const  theta
    1         x6   0    3   1   0  -1   1   0  -1     12      4
    1         x7   0   13   0  -1  -7   0   1  -7     28  28/13
    0         x1   1   -1   0   0   1   0   0   1      8    inf
              pi   0   16   1  -1  -8   1   1  -8     40       
          c - pi   0  -16  -1   1   8   0   0   9              
pivot(col = x2, row = x7)
--------------------------------------------------------------------------------
               c   0   0   0      0      0   1      1      1               
 base  base_name  x1  x2  x3     x4     x5  x6     x7     x8   const  theta
    1         x6   0   0   1   3/13   8/13   1  -3/13   8/13   72/13  72/13
    0         x2   0   1   0  -1/13  -7/13   0   1/13  -7/13   28/13    inf
    0         x1   1   0   0  -1/13   6/13   0   1/13   6/13  132/13    inf
              pi   0   0   1   3/13   8/13   1  -3/13   8/13   72/13       
          c - pi   0   0  -1  -3/13  -8/13   0  16/13   5/13               
pivot(col = x3, row = x6)
--------------------------------------------------------------------------------
               c   0   0   0      0      0   1      1      1               
 base  base_name  x1  x2  x3     x4     x5  x6     x7     x8   const  theta
    0         x3   0   0   1   3/13   8/13   1  -3/13   8/13   72/13       
    0         x2   0   1   0  -1/13  -7/13   0   1/13  -7/13   28/13       
    0         x1   1   0   0  -1/13   6/13   0   1/13   6/13  132/13       
              pi   0   0   0      0      0   0      0      0       0       
          c - pi   0   0   0      0      0   1      1      1               

x1 = 132/13
x2 = 28/13
x3 = 72/13
x4 = 0
x5 = 0
x6 = 0
x7 = 0
x8 = 0
min = 0
```
