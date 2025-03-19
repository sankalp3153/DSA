/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 313
 * Updated: 2025-03-19T12:54:23+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 313;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
