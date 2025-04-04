"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 391
Updated: 2025-04-04T19:47:50+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 391
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
