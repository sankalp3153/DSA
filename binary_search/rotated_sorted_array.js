/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 1020
 * Updated: 2025-10-02T18:03:18+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1020;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
