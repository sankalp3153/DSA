/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 2006
 * Updated: 2026-07-27T20:42:53+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2006;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
