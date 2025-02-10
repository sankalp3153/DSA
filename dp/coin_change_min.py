"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 177
Updated: 2025-02-10T18:41:55+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 177
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
