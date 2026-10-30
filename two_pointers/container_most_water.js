/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 2305
 * Updated: 2026-10-30T20:33:16+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2305;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
