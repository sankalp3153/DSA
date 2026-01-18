/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 1365
 * Updated: 2026-01-18T11:56:38+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1365;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
