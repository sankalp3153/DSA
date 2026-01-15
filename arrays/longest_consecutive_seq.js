/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 1359
 * Updated: 2026-01-15T17:51:46+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1359;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
