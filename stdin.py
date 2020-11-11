from typing import List
import numpy as np
from simplex import simplex, M
import sys
import sympy
sys.tracebacklimit = 0


def scanlist() -> List[str]:
    line = sys.stdin.readline().strip()
    return list(map(lambda e: e.strip(),
                    line.split(','))) if len(line) else []


def strlist2rationals(src: List[str]) -> List[sympy.Basic]:
    return list(map(sympy.parse_expr, src))


if __name__ == "__main__":
    print('シンプレックス法')
    MAX = input('最大化 or 最小化 (max or min)') == 'max'
    # 目的関数係数
    print('目的関数係数')
    c = np.array(strlist2rationals(scanlist()))
    c_name = [f'x{i+1}' for i in range(len(c))]

    # 制約条件係数行列
    print('制約条件係数行列 (空行で完了)')
    keisu = []
    while True:
        l = strlist2rationals(scanlist())
        if len(l) == 0:
            break
        else:
            keisu.append(l)

    m = np.array(keisu)

    # 基底変数
    print('基底変数')
    base_name = scanlist()
    base = np.array([c[c_name.index(e)] for e in base_name])

    simplex(MAX, c, c_name, m, base, base_name)
