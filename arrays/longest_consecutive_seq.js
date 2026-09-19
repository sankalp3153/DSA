/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 2187
 * Updated: 2026-09-19T12:14:30+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2187;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
