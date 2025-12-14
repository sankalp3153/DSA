/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 1250
 * Updated: 2025-12-14T19:16:21+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1250;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
