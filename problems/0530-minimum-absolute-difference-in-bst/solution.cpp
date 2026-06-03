class Solution {
public:

    int ans = INT_MAX;
    int num = -1;

int getMinimumDifference(TreeNode* root) {

    if (root->left != NULL)
        getMinimumDifference(root->left);

    if (num >= 0)
        ans = min(ans, root->val - num);

    num = root->val;

    if (root->right != NULL)
        getMinimumDifference(root->right);

      return ans;
    }
};