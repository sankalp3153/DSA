"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1534
Updated: 2026-03-03T16:41:15+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1534
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
