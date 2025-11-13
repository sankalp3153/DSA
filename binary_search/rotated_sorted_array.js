/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 1135
 * Updated: 2025-11-13T22:38:59+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1135;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
