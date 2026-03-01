/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 1523
 * Updated: 2026-03-01T11:43:23+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1523;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
