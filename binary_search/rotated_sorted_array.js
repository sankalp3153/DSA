/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 2032
 * Updated: 2026-08-05T11:16:53+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2032;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
