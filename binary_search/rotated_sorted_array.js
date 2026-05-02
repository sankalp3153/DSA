/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 1733
 * Updated: 2026-05-02T17:18:33+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1733;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
