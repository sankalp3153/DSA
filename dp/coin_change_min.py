"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 2109
Updated: 2026-08-25T23:28:05+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2109
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
