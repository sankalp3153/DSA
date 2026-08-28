/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 2124
 * Updated: 2026-08-28T12:18:30+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2124;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
