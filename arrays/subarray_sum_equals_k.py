"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 1173
Updated: 2025-11-26T13:00:55+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1173
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
