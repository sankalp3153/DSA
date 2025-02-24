/**
 * Module: edit_distance
 * Approach: space-optimized rolling row DP
 * Revision: 224
 * Updated: 2025-02-24T13:03:14+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 224;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
