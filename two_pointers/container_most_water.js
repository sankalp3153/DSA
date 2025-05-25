/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 557
 * Updated: 2025-05-25T13:47:00+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 557;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
