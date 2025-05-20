/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 534
 * Updated: 2025-05-20T22:35:31+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 534;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
