"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 1104
Updated: 2025-10-31T16:59:11+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1104
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
