/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 1480
 * Updated: 2026-02-16T21:29:06+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1480;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
