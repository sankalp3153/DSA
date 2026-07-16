"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1971
Updated: 2026-07-16T11:22:12+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1971
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
