/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 2236
 * Updated: 2026-10-03T13:55:55+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2236;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
