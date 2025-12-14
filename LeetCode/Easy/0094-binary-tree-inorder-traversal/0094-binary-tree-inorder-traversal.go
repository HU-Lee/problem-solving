/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func inorderTraversal(root *TreeNode) []int {
    if root == nil {
        return []int{}
    }
    result := []int{root.Val}
    if (root.Left != nil) {
        result = append(inorderTraversal(root.Left), result...)
    }
    if (root.Right != nil) {
        result = append(result, inorderTraversal(root.Right)...)
    }
    return result
}