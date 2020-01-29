// 函数复用
//必要条件，只需要考虑A[0],B[0]两个数
class Solution {
public:
    int check (int x, vector<int>& A, vector<int>& B){
        int cnt1=0;
        int cnt2=0;
        for (int j=0; j<A.size();++j){
            if(A[j]!=x && B[j]!=x) return 20001;
            if(A[j]==x && B[j]==x) continue;
            if(A[j]!=x) ++cnt1;
            if(B[j]!=x) ++cnt2;
        }
        return min(cnt1,cnt2);
    }
    int minDominoRotations(vector<int>& A, vector<int>& B) {
        int tmp1=check(A[0],A,B);
        int tmp2=check(B[0],A,B);
        int ans=min(tmp1,tmp2);
        if(ans>20000) return -1;
        return ans;
    }
};

