/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 1368
 * Updated: 2026-01-18T18:51:46+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1368;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
