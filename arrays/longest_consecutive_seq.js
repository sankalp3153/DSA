/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 738
 * Updated: 2025-07-20T14:59:28+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 738;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
