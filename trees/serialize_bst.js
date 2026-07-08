/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 1943
 * Updated: 2026-07-08T19:47:49+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1943;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
