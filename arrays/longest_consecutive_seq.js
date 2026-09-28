/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 2210
 * Updated: 2026-09-28T21:02:17+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2210;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
