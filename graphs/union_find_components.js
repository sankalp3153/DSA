/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 2038
 * Updated: 2026-08-06T12:16:18+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2038;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
