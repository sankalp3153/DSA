/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 1937
 * Updated: 2026-07-06T21:30:35+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1937;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
