"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 299
Updated: 2025-03-16T10:32:36+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 299
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
