/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 1529
 * Updated: 2026-03-02T15:00:46+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1529;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
