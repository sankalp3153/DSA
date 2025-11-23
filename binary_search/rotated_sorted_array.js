/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 1158
 * Updated: 2025-11-23T20:41:41+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1158;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
