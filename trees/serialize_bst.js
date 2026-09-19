/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 2196
 * Updated: 2026-09-19T22:31:41+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2196;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
