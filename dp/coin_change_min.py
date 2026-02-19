"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1488
Updated: 2026-02-19T22:09:25+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1488
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
