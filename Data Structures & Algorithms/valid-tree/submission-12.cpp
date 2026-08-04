class DSU {
public:
    vector<int> parent;
    vector<int> size;
    int component;
    DSU(int p) {
        for (int i = 0; i < p; i++) {
            parent.push_back(i);
        }
        size.assign(p, 1);
        component = p;
    }
    int find(int i) {
        if (parent[i] != i) {
            parent[i] = find(parent[i]);
        }
        return parent[i];
    }
    bool union_find(int i, int j) {
        int p = find(i), q = find(j);
        if (p == q) {
            return false;
        }
        if (size[p] > size[q]) {
            parent[q] = p;
            size[p] += size[q];
        } else {
            parent[p] = q;
            size[q] += size[p];
        }
        component -= 1;
        return true;
    }
};

class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        if ((int)edges.size() != n - 1) {return false;};
        DSU* dsu = new DSU(n);
        for (const auto& e : edges) {
            if (!dsu->union_find(e[0], e[1])) {
                return false;
            }
        }
        return dsu->component == 1;
    }
};
