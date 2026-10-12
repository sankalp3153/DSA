/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 2259
 * Updated: 2026-10-12T13:45:54+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2259;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
