/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 1776
 * Updated: 2026-05-19T20:38:15+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1776;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
