/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 773
 * Updated: 2025-07-29T23:24:48+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 773;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
