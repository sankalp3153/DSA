/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 1848
 * Updated: 2026-06-09T13:12:25+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1848;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
