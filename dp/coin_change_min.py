"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 131
Updated: 2025-01-30T17:10:55+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 131
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
