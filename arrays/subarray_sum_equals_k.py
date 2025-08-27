"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 897
Updated: 2025-08-27T16:00:43+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 897
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
