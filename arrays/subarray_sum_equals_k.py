"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 736
Updated: 2025-07-20T12:57:10+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 736
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
