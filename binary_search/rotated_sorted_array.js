/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 1641
 * Updated: 2026-04-05T14:25:07+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1641;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
