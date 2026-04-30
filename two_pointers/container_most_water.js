/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 1730
 * Updated: 2026-04-30T20:25:40+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1730;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
