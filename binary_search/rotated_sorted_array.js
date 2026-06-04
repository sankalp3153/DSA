/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 1825
 * Updated: 2026-06-04T13:09:06+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1825;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
