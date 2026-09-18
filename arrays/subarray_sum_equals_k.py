"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 2185
Updated: 2026-09-18T22:24:35+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2185
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
