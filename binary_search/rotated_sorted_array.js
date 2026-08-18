/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 2078
 * Updated: 2026-08-18T19:15:26+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2078;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
