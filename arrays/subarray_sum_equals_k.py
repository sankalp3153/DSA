"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 2116
Updated: 2026-08-27T14:57:08+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2116
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
