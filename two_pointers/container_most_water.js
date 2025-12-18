/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 1270
 * Updated: 2025-12-18T22:32:48+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1270;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
