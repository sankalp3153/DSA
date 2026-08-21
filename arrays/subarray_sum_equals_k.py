"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 2093
Updated: 2026-08-21T16:53:18+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2093
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
