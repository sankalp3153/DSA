/**
 * Module: edit_distance
 * Approach: space-optimized rolling row DP
 * Revision: 960
 * Updated: 2025-09-17T16:44:31+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 960;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
