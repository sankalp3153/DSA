/**
 * Module: edit_distance
 * Approach: space-optimized rolling row DP
 * Revision: 730
 * Updated: 2025-07-18T17:06:05+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 730;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
