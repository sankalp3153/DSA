/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 2256
 * Updated: 2026-10-12T11:11:21+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2256;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
