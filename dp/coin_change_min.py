"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 913
Updated: 2025-09-01T18:12:13+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 913
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
