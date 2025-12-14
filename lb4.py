def main():
    try:
        line = input().split()
        if not line:
            return
        
        iterator = map(int, line)
        n = next(iterator)
        m = next(iterator)
        
        tree = array('q', (0 for _ in range(n + 2)))
        
        for _ in range(m):
            try:
                line = input().split()
            except EOFError:
                break
                
            if not line:
                break
            
            iterator = map(int, line)
            op = next(iterator)
            
            if op == 1:
                l = next(iterator)
                r = next(iterator)
                v = next(iterator)
                
                idx = l + 1
                while idx <= n + 1:
                    tree[idx] += v
                    idx += idx & -idx
                
                idx = r + 1
                while idx <= n + 1:
                    tree[idx] -= v
                    idx += idx & -idx
            else:
                i = next(iterator)
                idx = i + 1
                res = 0
                while idx > 0:
                    res += tree[idx]
                    idx -= idx & -idx
                print(res)
                
    except (EOFError, StopIteration):
        pass

if __name__ == '__main__':
    main()