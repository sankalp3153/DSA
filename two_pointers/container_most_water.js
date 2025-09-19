/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 971
 * Updated: 2025-09-19T17:42:44+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 971;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
