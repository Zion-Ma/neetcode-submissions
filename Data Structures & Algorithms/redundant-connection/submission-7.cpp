class DSU {
public:
    vector<int> parent;
    vector<int> size;
    int component;
    DSU(int n) {
        component = n;
        for (int i = 0; i < n; i++) {
            parent.push_back(i);
        }
        size.assign(n, 1);
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
        component--;
        return true;
    }
};

class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        DSU dsu((int)edges.size() + 1);
        int x = 0, y = 0;
        for (const auto& e : edges) {
            if (!dsu.union_find(e[0], e[1])) {
                x = e[0];
                y = e[1];
                break;
            }
        }
        return {x, y};
    }
};
