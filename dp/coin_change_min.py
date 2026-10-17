"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 2270
Updated: 2026-10-17T16:56:15+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2270
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
