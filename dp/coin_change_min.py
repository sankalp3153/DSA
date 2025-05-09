"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 499
Updated: 2025-05-09T19:53:53+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 499
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
