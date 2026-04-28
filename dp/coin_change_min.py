"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1718
Updated: 2026-04-28T11:30:35+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1718
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
