/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 2127
 * Updated: 2026-08-28T20:49:09+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2127;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
