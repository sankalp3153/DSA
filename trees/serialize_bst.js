/**
 * Compact Preorder BST Codec (Serialize & Deserialize without null markers).
 * Time: O(n) | Space: O(n)
 */
export class BSTNode {
  constructor(val, left = null, right = null) {
    this.val = val;
    this.left = left;
    this.right = right;
  }
}

export function serializeBST(root) {
  const out = [];
  const preorder = (node) => {
    if (!node) return;
    out.push(node.val);
    preorder(node.left);
    preorder(node.right);
  };
  preorder(root);
  return out.join(",");
}

export function deserializeBST(data) {
  if (!data) return null;
  const vals = data.split(",").map(Number);
  let idx = 0;

  const build = (min, max) => {
    if (idx >= vals.length) return null;
    const val = vals[idx];
    if (val <= min || val >= max) return null;
    idx += 1;
    return new BSTNode(val, build(min, val), build(val, max));
  };

  return build(-Infinity, Infinity);
}
