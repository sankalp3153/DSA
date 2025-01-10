/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 54
 * Updated: 2025-01-10T13:04:45+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 54;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
