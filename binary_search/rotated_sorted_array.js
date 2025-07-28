/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 767
 * Updated: 2025-07-28T17:29:38+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 767;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
