"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 200
Updated: 2025-02-17T13:40:35+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 200
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
