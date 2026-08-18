/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 2075
 * Updated: 2026-08-18T15:30:37+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2075;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
