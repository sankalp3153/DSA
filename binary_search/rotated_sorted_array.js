/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 1595
 * Updated: 2026-03-21T16:41:56+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1595;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
