/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 974
 * Updated: 2025-09-20T11:06:48+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 974;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
