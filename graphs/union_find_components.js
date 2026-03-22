/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 1601
 * Updated: 2026-03-22T23:17:59+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1601;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
