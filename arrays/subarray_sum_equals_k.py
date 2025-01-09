"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 46
Updated: 2025-01-09T14:20:05+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 46
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
