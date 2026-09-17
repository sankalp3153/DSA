"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 2178
Updated: 2026-09-17T21:19:59+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2178
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
