class Solution:
    def simplifyPath(self, path: str) -> str:
        chunks = path.split('/')
        print(chunks)
        res = []
        for file in chunks:
            if file == "." or file == "":
                continue
            elif file == "..":
                if res:
                    res.pop()
            else:
                res.append(file)
        ans = '/' + '/'.join(res)
        return ans