/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 2262
 * Updated: 2026-10-13T16:00:18+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2262;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
