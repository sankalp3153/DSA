/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 1371
 * Updated: 2026-01-19T21:33:00+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1371;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
