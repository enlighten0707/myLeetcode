class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
        //第一个想法，hash表挂长链
        //如何查重：利用集合set操作
        //set的用法，pair的用法

        set<string> Set;

        for(int k=0;k<emails.size();++k){
            int j=0;
            while(emails[k][j]!='@'){
                if(emails[k][j]=='.') {
                    emails[k].erase(j,1);
                    continue;
                }
                else if(emails[k][j]=='+') break;
                ++j;
            }
            int i=j;
            while(j<emails[k].length() && emails[k][j]!='@') ++j;
            emails[k].erase(i,j-i);
            cout<<emails[k]<<'\n';
            Set.insert(emails[k]);
        }
        return Set.size();
        
     }
};

//Coding Tips:特殊情况处理，string的erase操作之后指针不需要移位，否则有跳跃