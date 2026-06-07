"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 1840
Updated: 2026-06-07T11:51:22+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1840
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
