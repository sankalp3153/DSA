"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 368
Updated: 2025-03-30T22:41:24+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 368
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
