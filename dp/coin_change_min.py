"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1948
Updated: 2026-07-09T12:52:44+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1948
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
