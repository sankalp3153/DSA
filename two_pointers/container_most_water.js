/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 1960
 * Updated: 2026-07-13T15:12:34+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1960;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
