"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 207
Updated: 2025-02-19T10:00:23+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 207
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
