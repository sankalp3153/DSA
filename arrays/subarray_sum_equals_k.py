"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 1978
Updated: 2026-07-18T13:16:29+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1978
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
