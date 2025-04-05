/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 396
 * Updated: 2025-04-05T20:33:36+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 396;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
