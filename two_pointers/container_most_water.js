/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 350
 * Updated: 2025-03-24T16:05:48+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 350;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
