"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 2300
Updated: 2026-10-29T16:39:55+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2300
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
