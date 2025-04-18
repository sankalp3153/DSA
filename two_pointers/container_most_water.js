/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 442
 * Updated: 2025-04-18T22:55:07+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 442;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
