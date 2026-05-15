/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 1759
 * Updated: 2026-05-15T18:31:59+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1759;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
