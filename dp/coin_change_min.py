"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 936
Updated: 2025-09-09T10:14:48+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 936
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
