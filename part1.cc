#include <cassert>
#include <string>
#include <iostream>
#include <algorithm>
#include <iterator>
#include <array>
#include <functional>
#include <ranges>
#include <cmath>
#include <vector>

bool ends_with(std::string const &value, std::string const &needle)
{
    if (needle.size() > value.size())
    {
        return false;
    }
    return std::equal(needle.rbegin(), needle.rend(), value.rbegin());
}

// Recursive function (sorry) to generate all permutations (or better the
// cartesian product) of all characters in given input sequence.
void permute(const std::string &sequence, std::string prefix, const std::size_t repeat, std::vector<std::string> &res)
{
    if (repeat == 0)
    {
        res.push_back(prefix);
        return;
    }

    for (auto i = 0; i < sequence.size(); i++)
    {
        std::string new_prefix = prefix + sequence[i];
        permute(sequence, new_prefix, repeat - 1, res);
    }
}

// Produce all permutations of given sequence of characters into a vector and
// return it.
std::vector<std::string> permutations(const std::string &sequence, const std::size_t repeat)
{
    const auto no_of_permutations = std::pow(sequence.length(), repeat);
    std::vector<std::string> buf;
    buf.reserve(no_of_permutations);
    permute(sequence, "", repeat, buf);
    assert(buf.size() == no_of_permutations);
    return buf;
}

std::string determine_pattern(const std::string &states, const std::size_t window_width)
{
    std::string buf;
    const auto buf_len = std::pow(states.length(), window_width);
    const auto perms = permutations(states, window_width);
    for (const auto &elem : perms)
    {
        if (buf.empty())
        {
            buf = elem;
        }

        if (buf.find(elem) == std::string::npos)
        {
            auto i = 0;
            while (i < window_width)
            {
                const auto pos = window_width - i;
                const std::string head = elem.substr(0, pos);
                const std::string tail = elem.substr(pos);
                if (ends_with(buf, head))
                {
                    buf.append(tail);
                    break;
                }

                i++;
                if (i == window_width)
                {
                    buf.append(elem);
                    break;
                }
            }
        }
    }
    const auto res = buf.substr(0, buf_len - window_width) + perms.back();
    return res;
}

int main()
{
    assert(determine_pattern(".X", 3) == "...X.XXX");
    assert(determine_pattern(".xO", 4) == "....x...O..xx..xO..Ox..OO.x.x.O.xxx.xxO.xOx.xOO.O.Oxx.OxO.OOx.OOOxxxxOxxOOxOxOOOO");
}
