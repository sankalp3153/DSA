/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 1707
 * Updated: 2026-04-23T18:50:00+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1707;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
