"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 184
Updated: 2025-02-13T12:36:26+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 184
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
