/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 1460
 * Updated: 2026-02-11T12:57:55+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1460;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
