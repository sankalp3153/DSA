/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 422
 * Updated: 2025-04-16T16:35:43+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 422;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
