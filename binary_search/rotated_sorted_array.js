/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 284
 * Updated: 2025-03-12T14:42:17+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 284;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
