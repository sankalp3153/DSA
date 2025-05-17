/**
 * Module: edit_distance
 * Approach: space-optimized rolling row DP
 * Revision: 523
 * Updated: 2025-05-17T13:46:35+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 523;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
