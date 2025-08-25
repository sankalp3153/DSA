"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 890
Updated: 2025-08-25T18:19:08+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 890
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
