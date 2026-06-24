/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 1900
 * Updated: 2026-06-24T11:13:05+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1900;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
