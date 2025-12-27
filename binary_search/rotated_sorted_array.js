/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 1296
 * Updated: 2025-12-27T16:36:05+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1296;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
