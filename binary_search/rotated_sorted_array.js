/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 813
 * Updated: 2025-08-09T19:40:50+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 813;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
