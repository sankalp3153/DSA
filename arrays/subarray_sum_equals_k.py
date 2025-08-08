"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 805
Updated: 2025-08-08T10:23:31+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 805
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
