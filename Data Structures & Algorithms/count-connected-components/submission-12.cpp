class DSU {
public:
    vector<int> parent;
    vector<int> size;
    int component;
    DSU(int n) {
        for (int i = 0; i < n; i++) {
            parent.push_back(i);
            size.assign(n, 1);
            component = n;
        }
    }
    // find the parent of i
    int find(int i) {
        if (parent[i] != i) {
            parent[i] = find(parent[i]);
        }
        return parent[i];
    }
    // union 2 trees
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
        component--;
        return true;
    }
};

class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        DSU dsu(n);
        for (auto& e : edges) {
            bool _ = dsu.union_find(e[0], e[1]);
        }
        return dsu.component;
    }
};
