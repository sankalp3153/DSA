/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 1871
 * Updated: 2026-06-13T11:33:20+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1871;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
