/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 2311
 * Updated: 2026-10-31T21:37:16+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2311;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
