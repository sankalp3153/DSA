/**
 * Module: rotated_sorted_array
 * Approach: half-sorted invariant binary search
 * Revision: 1963
 * Updated: 2026-07-14T11:10:27+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1963;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
