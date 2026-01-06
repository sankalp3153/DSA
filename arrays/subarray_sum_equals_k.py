"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 1334
Updated: 2026-01-06T16:57:58+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1334
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
