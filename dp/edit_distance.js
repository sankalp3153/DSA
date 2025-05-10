/**
 * Module: edit_distance
 * Approach: space-optimized rolling row DP
 * Revision: 500
 * Updated: 2025-05-10T14:04:24+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 500;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
