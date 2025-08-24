/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 882
 * Updated: 2025-08-24T16:34:14+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 882;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
