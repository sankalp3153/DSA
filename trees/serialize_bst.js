/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 1437
 * Updated: 2026-02-05T19:39:07+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1437;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
