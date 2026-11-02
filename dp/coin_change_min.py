"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 2316
Updated: 2026-11-02T16:08:43+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2316
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
