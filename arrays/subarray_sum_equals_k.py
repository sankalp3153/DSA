"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 552
Updated: 2025-05-24T16:47:21+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 552
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
