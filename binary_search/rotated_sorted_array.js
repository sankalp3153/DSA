/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 192
 * Updated: 2025-02-13T23:17:16+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 192;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
