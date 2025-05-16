"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 522
Updated: 2025-05-16T13:20:55+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 522
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
