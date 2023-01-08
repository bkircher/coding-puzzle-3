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


def determine_pattern(states: str, window_length: int) -> str:
    buffer = None
    buf_len = pow(len(states), window_length)
    perms = permutations(sequence=states, repeat=window_length)
    for elem in perms:
        if not buffer:
            buffer = elem

        if elem not in buffer:
            i = 1
            while i < window_length:
                pos = window_length - i
                head, tail = elem[:pos], elem[pos:]
                if buffer[-pos:] == head:
                    buffer += tail
                    break

                i += 1
                if i == window_length:
                    buffer += elem
                    break

    res = buffer[: buf_len - window_length] + perms[-1]
    return res


assert determine_pattern(".X", 3) == "...X.XXX"
assert determine_pattern(".xO", 4) == "....x...O..xx..xO..Ox..OO.x.x.O.xxx.xxO.xOx.xOO.O.Oxx.OxO.OOx.OOOxxxxOxxOOxOxOOOO"
