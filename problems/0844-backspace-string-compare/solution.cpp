class Solution {
public:
    int nextChar(std::string str, int cur) {
        while (cur > -1 && str[cur] == '#') {
            int cnt = 1;
            cur--;
            while (cur > -1 && cnt > 0) {
                if (str[cur] == '#') {
                    cnt++;
                } else {
                    cnt--;
                }
                cur--;
            }
        }
        return cur;
    }

    bool backspaceCompare(std::string s, std::string t) {
        int i = nextChar(s, s.length() - 1);
        int j = nextChar(t, t.length() - 1);

        while (i > -1 && j > -1) {
            if (s[i] != t[j]) {
                return false;
            }
            i = nextChar(s, i - 1);
            j = nextChar(t, j - 1);
        }

        return i == -1 && j == -1;
    }
};