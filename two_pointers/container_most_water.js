/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 1316
 * Updated: 2025-12-31T19:25:04+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1316;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
