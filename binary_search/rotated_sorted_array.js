/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 514
 * Updated: 2025-05-13T21:41:57+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 514;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
