class Solution {
public:
    //贪心算法
    int update(int i,string source,string target){
        int j=0;
        while(i<target.length() &&j< source.length()){
            if(target[i]==source[j]){
                i++;
                j++;
            }
            else j++;
        }
        return i;
    }
    int shortestWay(string source, string target) {
        int i=0;
        int ans=0;
        while(i<target.length()){
            ++ans;
            int tmp=update(i,source,target);
            if(tmp==i) return -1;
            else i=tmp;
        }
        return ans;
    }
};
