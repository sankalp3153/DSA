/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 304
 * Updated: 2025-03-16T18:05:21+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 304;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
