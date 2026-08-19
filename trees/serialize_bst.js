/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 2081
 * Updated: 2026-08-19T11:41:49+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2081;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
