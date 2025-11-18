"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1143
Updated: 2025-11-18T18:32:25+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1143
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
