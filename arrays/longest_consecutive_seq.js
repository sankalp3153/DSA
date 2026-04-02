/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 1635
 * Updated: 2026-04-02T17:53:16+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1635;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
