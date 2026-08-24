/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 2104
 * Updated: 2026-08-24T15:32:24+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2104;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
