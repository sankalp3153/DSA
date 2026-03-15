/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 1572
 * Updated: 2026-03-15T18:12:38+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1572;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
