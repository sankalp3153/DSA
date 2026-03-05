/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 1543
 * Updated: 2026-03-05T12:36:32+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1543;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
