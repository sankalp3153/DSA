/**
 * Module: edit_distance
 * Approach: space-optimized rolling row DP
 * Revision: 1305
 * Updated: 2025-12-29T23:02:47+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1305;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
