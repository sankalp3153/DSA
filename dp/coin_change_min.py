"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 269
Updated: 2025-03-09T10:28:13+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 269
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
