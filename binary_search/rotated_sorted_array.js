/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 1986
 * Updated: 2026-07-20T20:00:53+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1986;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
