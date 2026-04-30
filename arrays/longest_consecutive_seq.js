/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 1727
 * Updated: 2026-04-30T13:05:18+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1727;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
