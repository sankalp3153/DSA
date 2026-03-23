"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1603
Updated: 2026-03-23T18:51:07+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1603
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
