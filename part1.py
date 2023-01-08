from typing import List
from itertools import product


def permutations(sequence: str, repeat: int) -> List[str]:
    """Produce all permutations of given input sequence into a list.

    Actually the cartesian product of the input. Roughly equivalent to nested
    for-loops in a generator expression or can be done recursively.

    Example:

    permutations(".X", 3) → ['...', '..X', '.X.', '.XX', 'X..', 'X.X', 'XX.', 'XXX']

    """
    return ["".join(tup) for tup in product(sequence, repeat=repeat)]


def determine_pattern(states: str, window_width: int) -> str:
    buf = None
    buf_len = pow(len(states), window_width)
    perms = permutations(sequence=states, repeat=window_width)
    for elem in perms:
        if not buf:
            buf = elem

        if elem not in buf:
            i = 1
            while i < window_width:
                pos = window_width - i
                head, tail = elem[:pos], elem[pos:]
                if buf[-pos:] == head:
                    buf += tail
                    break

                i += 1
                if i == window_width:
                    buf += elem
                    break

    res = buf[: buf_len - window_width] + perms[-1]
    return res


assert determine_pattern(".X", 3) == "...X.XXX"
assert determine_pattern(".xO", 4) == "....x...O..xx..xO..Ox..OO.x.x.O.xxx.xxO.xOx.xOO.O.Oxx.OxO.OOx.OOOxxxxOxxOOxOxOOOO"
