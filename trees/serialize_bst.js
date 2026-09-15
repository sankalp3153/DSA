/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 2173
 * Updated: 2026-09-15T19:11:05+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2173;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
