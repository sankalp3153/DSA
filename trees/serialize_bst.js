/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 1345
 * Updated: 2026-01-09T19:20:23+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1345;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
