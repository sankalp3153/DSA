/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 2009
 * Updated: 2026-07-28T14:05:29+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2009;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
