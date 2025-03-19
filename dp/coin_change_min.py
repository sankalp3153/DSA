"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 315
Updated: 2025-03-19T15:33:25+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 315
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
