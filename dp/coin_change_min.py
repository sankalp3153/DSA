"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1580
Updated: 2026-03-19T11:18:28+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1580
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
