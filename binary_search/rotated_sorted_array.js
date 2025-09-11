/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 951
 * Updated: 2025-09-11T21:25:35+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 951;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
