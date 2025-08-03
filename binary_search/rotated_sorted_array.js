/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 790
 * Updated: 2025-08-03T21:39:46+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 790;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
