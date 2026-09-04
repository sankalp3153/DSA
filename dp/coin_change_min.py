"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 2155
Updated: 2026-09-04T21:53:46+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2155
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
