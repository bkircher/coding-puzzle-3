# coding-puzzle-3

Another puzzle.

We would like to give you a small programming task to learn a bit more about your current skills in the C++ environment. Please choose one of the given Tasks.
If you have any questions, please do not hesitate to contact us. We would estimate a processing time of about 1 week (+-1-2 days is no problem). It is not necessary to have a complete and perfect solution for the second tasks. We want to know how you approach such a problem and then try to implement your "concept".

## Part 1

Write the function

```c++
std::string determine_pattern(const std::string &states, const std::size_t window_width)
```

that determines the longest string that satisfies the following conditions:

- All characters of the argument states occur in the output string (string).
- Each substring of length window_width occurs only once in the output string.

Note: The pattern forms a ring.

Examples:

```raw
determine_pattern(".X", 3) = ...X.XXX (length 8)
determine_pattern(".xO", 4) = ....x...O..xx..xO..Ox..OO.x.x.O.xxx.xxO.xOx.xOO.O.Oxx.OxO.OOx.OOOxxxxOxxOOxOxOOOO (length 81)
```

### Run

I forgot almost all my C++ but I thing this works:

```sh
c++ --std=c++17 part1.cc && ./a.out
```

The Python version is just

```sh
python past1.py
```

## Part 2

Later.
