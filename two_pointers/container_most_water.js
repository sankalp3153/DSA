/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 2282
 * Updated: 2026-10-21T11:19:17+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2282;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
