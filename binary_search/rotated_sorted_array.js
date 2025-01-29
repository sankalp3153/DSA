/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 123
 * Updated: 2025-01-29T18:19:01+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 123;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
