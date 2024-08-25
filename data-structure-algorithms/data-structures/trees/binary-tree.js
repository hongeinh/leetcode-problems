class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

class BinaryTree {
  constructor(val) {
    this.root = new Node(val);
    this.tree_height = 0;
  }

  insert(val) {
    let queue = [];
    if (this.root) queue.push(this.root);
    while (queue.length !== 0) {
      let node = queue.shift();

      // first case, if left is empty -> create new node, insert val & break
      if (!node.left) {
        const newNode = new Node(val);
        node.left = newNode;
        break;
      }

      if (!node.right) {
        const newNode = new Node(val);
        node.right = newNode;
        break;
      }

      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }
    return this;
  }

  // left root right
  inorder_depth_first_search(val, node) {
    if (!node) return false;
    const leftSearch = this.inorder_depth_first_search(val, node.left);
    if (leftSearch) return true;
    // root search
    if (node.val === val) return true;
    const rightSearch = this.inorder_depth_first_search(val, node.right);
    if (rightSearch) return true;
    // cant find any
    return false;
  }

  // root left right
  preorder_depth_first_search(val, node) {
    if (!node) return false;
    // root search first
    if (node.val === val) return true;
    // if cant find then we move left
    const leftSearch = this.preorder_depth_first_search(val, node.left);
    if (leftSearch) return true;
    // left cant find -> move right
    const rightSearch = this.preorder_depth_first_search(val, node.right);
    if (rightSearch) return true;
    // cant find any -> false
    return false;
  }

  // left right root
  postorder_depth_first_search(val, node) {
    if (!node) return false;
    // left search first
    const leftSearch = this.postorder_depth_first_search(val, node.left);
    if (leftSearch) return true;
    // if cant find left -> search right
    const rightSearch = this.postorder_depth_first_search(val, node.right);
    if (rightSearch) return true;
    // search root
    if (node.val === val) return true;
    return false;
  }

  // vist each level first, can try using queue
  breadth_first_search(val) {
    let queue = [];
    // visit root, then push left & right to traverse the entire level first
    if (this.root) queue.push(this.root);
    while (queue.length !== 0) {
      const node = queue.shift();
      if (node.val === val) return true;
      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }
    return false;
  }

  get_tree_height(node) {
    const maxVertices = this._get_tree_height(node);
    return maxVertices - 1;
  }

  // total edges of longest path from root to leaf
  _get_tree_height(node) {
    if (!node) return 0;
    const leftHeight = this._get_tree_height(node.left);
    const rightHeight = this._get_tree_height(node.right);
    return Math.max(leftHeight, rightHeight) + 1;
  }

  // val of the node we want to calculate depth
  get_tree_depth(val) {}
}

const tree = new BinaryTree(5);

tree.insert(4).insert(2).insert(3).insert(9);

console.log(
  tree.inorder_depth_first_search(10, tree.root),
  tree.inorder_depth_first_search(3, tree.root),
  tree.inorder_depth_first_search(2, tree.root),
  tree.inorder_depth_first_search(5, tree.root)
);
console.log(
  tree.preorder_depth_first_search(10, tree.root),
  tree.preorder_depth_first_search(3, tree.root),
  tree.preorder_depth_first_search(2, tree.root),
  tree.preorder_depth_first_search(5, tree.root)
);

console.log(
  tree.postorder_depth_first_search(10, tree.root),
  tree.postorder_depth_first_search(3, tree.root),
  tree.postorder_depth_first_search(2, tree.root),
  tree.postorder_depth_first_search(5, tree.root)
);

console.log(
  tree.breadth_first_search(10),
  tree.breadth_first_search(3),
  tree.breadth_first_search(2),
  tree.breadth_first_search(5)
);

console.log(tree.get_tree_height(tree.root));
