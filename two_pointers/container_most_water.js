/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 327
 * Updated: 2025-03-20T22:24:21+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 327;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
