"""
Circular Gas Station Tour via greedy running-deficit reset.
Time: O(n) | Space: O(1)
"""

from typing import List


def can_complete_circuit(gas: List[int], cost: List[int]) -> int:
    if sum(gas) < sum(cost):
        return -1

    start = 0
    tank = 0
    for idx, (g, c) in enumerate(zip(gas, cost)):
        tank += g - c
        if tank < 0:
            start = idx + 1
            tank = 0
    return start
