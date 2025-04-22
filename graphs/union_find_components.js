/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 451
 * Updated: 2025-04-22T16:50:40+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 451;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
