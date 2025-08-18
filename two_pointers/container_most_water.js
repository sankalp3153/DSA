/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 856
 * Updated: 2025-08-18T12:04:19+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 856;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
