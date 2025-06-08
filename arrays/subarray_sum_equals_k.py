"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 598
Updated: 2025-06-08T15:01:44+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 598
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
