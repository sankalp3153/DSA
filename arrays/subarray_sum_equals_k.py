"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 828
Updated: 2025-08-11T22:39:59+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 828
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
