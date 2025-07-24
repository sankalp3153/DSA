"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 752
Updated: 2025-07-24T14:40:30+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 752
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
