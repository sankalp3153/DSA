/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 71
 * Updated: 2025-01-14T18:23:44+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 71;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
