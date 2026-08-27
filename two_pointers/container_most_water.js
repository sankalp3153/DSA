/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 2121
 * Updated: 2026-08-27T20:28:53+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2121;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
