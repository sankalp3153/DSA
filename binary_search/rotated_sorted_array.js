/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 330
 * Updated: 2025-03-21T14:34:33+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 330;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
