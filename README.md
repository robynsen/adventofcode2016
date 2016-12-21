# adventofcode2016
Advent of Code 2016 solutions

| File | Description |
| --- | --- |
| `aoc01-part1.py` | Finds distance between start and end locations. Stores orientation and (x,y) distance from origin while parsing input. |
| `aoc01-part2.py` | Finds first location visited twice. Works similarly to Part 1 solution, with an list of visited sites updated and checked with each parsed instruction. |
| `aoc02-part1.py` | Square keypad instruction parser. Updates the position if the current position and next move instruction point to a different button. |
| `aoc02-part2.py` | Diamond keypad instruction parser. Similar to Part 1 solution, but now with different rules for position updates, and prints the output in hex. |
| `aoc03-part1.py` | Counts how many rows of input describe triangles that have the sum of the two smallest sides lengths greater than the longest side. |
| `aoc03-part2.py` | Similar to Part 1 solution. Now reads three rows of input at a time, and does a check similar to Part 1 but now on each of those three columns. |
| `aoc04-part1.py`  | Uses a regex to get the name, sector ID, and checksum. Uses collections.Counter.most_common and a custom sort (numerical desc, alphabetical asc) to compare against the given checksum. |
| `aoc04-part2.py`  | Similar to Part 1 solution. Now with shift decoder. |
