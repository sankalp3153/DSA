/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 2265
 * Updated: 2026-10-16T13:34:33+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2265;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
