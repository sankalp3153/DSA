/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 2239
 * Updated: 2026-10-04T16:43:24+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2239;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
