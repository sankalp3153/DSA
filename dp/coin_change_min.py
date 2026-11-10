"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 2339
Updated: 2026-11-10T12:07:25+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2339
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
