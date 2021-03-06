# adventofcode2016
Advent of Code 2016 solutions, in Python since I haven't used it before.

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
| `aoc05-part1.py`  | Simple password finder. |
| `aoc05-part2.py`  | Similar to Part 1 solution, with updated password builder. |
| `aoc06-part1.py`  | Uses zip to transpose input rows, with collections.Counter.most_common used on columns to find most common character. |
| `aoc06-part2.py`  | Similar to Part 1 solution, with most_common used to find least common character. |
| `aoc07-part1.py`  | Counts number of input rows satisfying the ABBA string requirements. |
| `aoc07-part2.py`  | Similar to Part 1 solution, with updated match conditions. |
| `aoc08-part1.py`  | Manual row rotation, with column rotation = transpose(rotate_row(transpose(A))) |
| `aoc08-part2.py`  | Similar to Part 1 solution, with new function to print the final output. |
| `aoc09-part1.py`  | Literal implementation of decompression. |
| `aoc09-part2.py`  | Calculates the expected decompressed length only, without actually decompressing. |
| `aoc10-part1.py`  | Uses a handful of dictionaries to store bot states and instructions. Ignores which chips go to which outputs, instead just removes them from the bot. |
| `aoc10-part2.py`  | Similar to Part 1 solution, now storing which chips go to outputs 0-2, and running to completion (i.e. until there are no further chip pairs for bots to hand over). |
| `aoc11-part1.py` |  |
| `aoc11-part2.py` |  |
| `aoc12-part1.py` |  |
| `aoc12-part2.py` |  |
| `aoc13-part1.py` | Breadth first search in Python to find distance from A to B. |
| `aoc13-part2.py` | Minor change from Part 1. BFS in Python that builds the tree of all unique nodes within 50 hops of the origin. |
| `aoc14.py` | Generates and stores hashes so each hash is generated only once. Checks ahead for solutions when triplet characters are found (rather than behind when quintuplets are found) so that the script only computes strictly as many hashes as are required to find the solution. Solutions to Part 1 and 2 in the single file. |
| `aoc15.py` | Finds solution via modular arithmetic. Solutions to Part 1 and 2 in the single file. |
| `aoc16-part1.py` | Literal implementation of the string expansion and reduction. Life is too short to wait for this to solve Part 2. |
| `aoc16-part2.py` | Uses a more efficient approach to building the dragon curve string, and reducing to the checksum. <br/><br/>Note the checksum calculation can be simplified as follows: <br/>1. Split the input string into `n`-many chunks of length `m`, where `n` is the largest odd divisor of `len(input)`<br/>2. For each of these `m`-long chunks of digits `abcd...x`, the chunk reduces to its final checksum digit using: sum of digits + half the length of input string + 1 % 2 = `(sum(a..x) + m/2 + 1) % 2` |
| `aoc17.py` | BFS to find: <br/>1. Directions along the shortest path to the goal coordinates<br/>2. Length of longest path to the goal coordinates |
| `aoc18.py` | Straightforward implementation of the logic to determine how many safe tiles are on the map. Solutions to Part 1 and 2 in the single file. |
| `aoc19.py` | For both parts, I looked for the pattern that emerged over the course of deletions, since I could see that a simple equivalent deletion pattern would emerge that would let me avoid a literal implementation of the given logic. I could see that:<br/><ol><li>For Part 1, the deletion pattern is a repeated loop of the following:<br/><ul><li>Check the number of indices (list length)</li><li>Delete every second index</li><li>If the initial list length was odd, delete the first index</li><li>Repeat until one item remains in the list</li></ul></li><li>For Part 2, the deletion pattern is a variant of deleting the first two of every three indices:<br/><ul><li>In the initial loop, apply the deletion pattern for the second half of the list</li><li>In the following loops, apply the deletion pattern across the whole list.</li><li>Repeat until one item remains in the list</li></ul></li></ol>Minimal customisation was required to cater to both odd and even numbers in both cases.<br/>Solutions to Part 1 and 2 in the single file. |
| `aoc20.py` | Not a particularly thrilling solution. This sorts the ranges by the lower value, and then for each range, compares the upper value against the lower value of the next range in sequence to detect gaps (i.e. allowed IPs). Solutions to Part 1 and 2 in the single file. |
