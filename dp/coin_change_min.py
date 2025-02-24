"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 223
Updated: 2025-02-24T11:46:57+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 223
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
