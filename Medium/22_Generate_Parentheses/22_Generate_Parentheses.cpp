class Solution {
public:
    typedef struct node {
        int Value;
        char Parentheses;
        struct node *Left; 
        struct node *Right;
    } Node;

    Node *NewNode(int value, char parentheses) {
        Node *node = new Node();
        node->Value = value;
        node->Parentheses = parentheses;
        node->Left = NULL;
        node->Right = NULL;

        return node;
    }

    Node *BuildTree(int value, int left, char parentheses){
        Node *temp = NewNode(value, parentheses);
        if(parentheses == '('){
            left++;
        }
        else{
            left--;
            value--;
        }
        if(value != 0){
            if(value == left){
                temp->Right = BuildTree(value, left, ')');
            }
            else if(left == 0){
                temp->Left = BuildTree(value, left, '(');
            }
            else{
                temp->Left = BuildTree(value, left, '(');
                temp->Right = BuildTree(value, left, ')');
            }
        }
        else{
            return temp;
        }
        return temp;
    }

    void TreeTraversal(Node *root, string s, vector<string> &answer){
        if(root->Left == NULL && root->Right == NULL){
            answer.push_back(s+root->Parentheses);
            return;
        }
        if(root->Left != NULL){
            TreeTraversal(root->Left, s+root->Parentheses, answer);
        }
        if(root->Right != NULL){
            TreeTraversal(root->Right, s+root->Parentheses, answer);
        }
        return;
    }

    vector<string> generateParenthesis(int n) {
        vector<string> answer;
        string temp = "";
        Node *root = BuildTree(n, 0, '(');
        TreeTraversal(root, temp, answer);

        return answer;
    }
};