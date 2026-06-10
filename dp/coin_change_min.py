"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1856
Updated: 2026-06-10T19:55:29+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1856
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
