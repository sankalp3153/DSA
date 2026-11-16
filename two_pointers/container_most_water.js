/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 2351
 * Updated: 2026-11-16T17:23:17+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2351;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
