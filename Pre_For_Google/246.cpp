//string的用法，string+可以是string/char
//int/char 的类型

class Solution {
public:
    bool isStrobogrammatic(string num) {
        unordered_map<char,char> Map;
        Map['0']='0';
        Map['1']='1';
        Map['6']='9';
        Map['8']='8';
        Map['9']='6';

        string str="";
        for(int i=num.size()-1;i>=0;--i){
            if(Map.count(num[i])==0) return false;
            else str+=Map[num[i]];
        }
        if(str==num) return true;
        return false;
    }
};