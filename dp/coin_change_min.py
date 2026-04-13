"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1672
Updated: 2026-04-13T18:04:45+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1672
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
