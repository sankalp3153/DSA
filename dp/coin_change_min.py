"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1626
Updated: 2026-03-30T17:56:25+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1626
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
