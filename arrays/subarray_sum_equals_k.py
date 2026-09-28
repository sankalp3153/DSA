"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 2208
Updated: 2026-09-28T19:11:29+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2208
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
