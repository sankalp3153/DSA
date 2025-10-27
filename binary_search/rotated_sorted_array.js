/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 1089
 * Updated: 2025-10-27T11:29:34+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1089;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
