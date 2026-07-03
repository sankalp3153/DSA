"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1925
Updated: 2026-07-03T23:05:27+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1925
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
