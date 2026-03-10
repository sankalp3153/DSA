/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 1555
 * Updated: 2026-03-10T12:11:27+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1555;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
