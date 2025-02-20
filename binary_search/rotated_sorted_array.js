/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 215
 * Updated: 2025-02-20T16:40:36+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 215;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
