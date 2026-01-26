/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 1391
 * Updated: 2026-01-26T10:57:33+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1391;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
