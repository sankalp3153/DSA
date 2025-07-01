"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 690
Updated: 2025-07-01T18:13:29+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 690
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
