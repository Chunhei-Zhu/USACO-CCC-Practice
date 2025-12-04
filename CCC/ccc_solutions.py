import sys

# =============================================================================
# CCC Solutions
# =============================================================================

# ================================
# CCC 2018 S2 – Sunflowers
# Link: https://dmoj.ca/problem/ccc18s2
# ================================

def mat90(num,mat):
    n = num
    for _ in range(4):
        if check(n,mat):
            return mat
        nmat = []           
        for row in zip(*mat[::-1]):    
            nmat.append(list(row))  
        mat = nmat
    return mat                   

def check(num,mat):
    n = num
    for i in range(n):
        for x in range(n-1):
            if mat[i][x] > mat[i][x+1]:
                return False
    for i in range(n):
        for x in range(n-1):
            if mat[x][i] > mat[x+1][i]:
                return False
    return True

def solve_sunflowers():
    print('Enter Test Data To 6.Sunflowers')
    try:
        num = int(input().strip())
        mat = [list(map(int, input().split())) for _ in range(num)]
        ans = mat90(num,mat)
        for row in ans:
            print(*row)
    except: pass

#solve_sunflowers()

# ================================
# CCC 2017 J4 – Favourite Times (Practice)
# Link: https://dmoj.ca/problem/ccc17j4
# ================================

def solve_favourite_times():
    print('Enter Test Data To 8.Favourite Time')
    try:
        num = int(input().strip())
        hour = 12
        minute = 0
        a = 0
        for i in range(num):
            minute += 1
            if minute > 59:
                minute = 0
                hour += 1
                if hour > 12:
                    hour = 1
            h1 = hour // 10     
            h2 = hour % 10   
            m1 = minute // 10  
            m2 = minute % 10 
            if hour < 10:
                clock = [h2, m1, m2] 
                if clock[1] - clock[0] == clock[2] - clock[1]:
                    a += 1
            else:
                clock = [h1, h2, m1, m2]
                if clock[1] - clock[0] == clock[2] - clock[1] == clock[3] - clock[2]:
                    a += 1
        print(a)
    except: pass

#solve_favourite_times()

# ================================
# CCC 2025 J3 – Product Codes
# Link: https://dmoj.ca/problem/ccc25j3
# ================================

def cap(s):
    caps = []
    for ch in s:
        if ch.isupper():
            caps.append(ch)
    caps = ''.join(caps)
    return caps

def num(s):
    total = 0
    i = 0
    L = len(s)
    while i < L:
        sign = 1
        if s[i] == '-' and i + 1 < L and s[i + 1].isdigit():
            sign = -1
            i += 1 
        if i < L and s[i].isdigit():
            val = 0
            while i < L and s[i].isdigit():
                val = val * 10 + int(s[i])
                i += 1
            total += sign * val
        else:
            i += 1
    return total

def solve_product_codes():
    print('Enter Test Data To 9.product codes')
    try:
        n = int(input().strip())
        s = [input().strip() for _ in range(n)]
        print('')
        print('Output')
        for ch in s:
            caps = cap(ch)
            nums = num(ch)
            print(f"{caps}{nums}")
    except: pass

#solve_product_codes()

# ================================
# CCC 2019 J2 – Time to Decompress
# Link: https://dmoj.ca/problem/ccc19j2
# ================================

def solve_time_to_decompress():
    print('Enter Test Data To 10.Time to Decompress')
    try:
        num = int(input().strip())
        data = [input().split() for _ in range(num)]
        for n, s in data:
            n = int(n)
            print(s * n)
    except: pass

#solve_time_to_decompress()

# ================================
# CCC 2021 J1 – Boiling Water
# Link: https://dmoj.ca/problem/ccc21j1
# ================================

def solve_boiling_water():
    print('Enter Test Data To 11.Boiling Water')
    try:
        b = int(input())
        p = 5 * b - 400
        print(p)
        if p > 100:
            print(1)
        elif p == 100:
            print(0)
        else:
            print(-1)
    except: pass

#solve_boiling_water()

# ============================================
# CCC 2020 Senior 2: Escape Room
# Link: https://cemc.uwaterloo.ca/contests/computing/2020/stage%201/seniorEn.pdf
# ============================================

def solve_escape_room():
    try:
        header = input().split()
        if not header: return
        R, C = map(int, header)
        grid = [list(map(int, input().split())) for _ in range(R)]

        stack = [(1, 1)]
        visited = set([(1, 1)])

        while stack:
            r, c = stack.pop()
            if (r, c) == (R, C):
                print("yes")
                return

            v = grid[r - 1][c - 1]

            i = 1
            while i * i <= v:
                if v % i == 0:
                    r1, c1 = i, v // i
                    if 1 <= r1 <= R and 1 <= c1 <= C and (r1, c1) not in visited:
                        visited.add((r1, c1))
                        stack.append((r1, c1))

                    r2, c2 = v // i, i
                    if (r2, c2) != (r1, c1):
                        if 1 <= r2 <= R and 1 <= c2 <= C and (r2, c2) not in visited:
                            visited.add((r2, c2))
                            stack.append((r2, c2))
                i += 1

        print("no")
    except: pass

#solve_escape_room()

# ===============================================================
# CCC 2016 S2: Tandem Bicycle
# Link: https://dmoj.ca/problem/ccc16s2
# ===============================================================

def low_high(num,nums):
    for i in range(num):
        for x in range(i + 1, num):
            if nums[i] > nums[x]:
                nums[i], nums[x] = nums[x], nums[i] 
    return nums

def high_low(num,nums):
    for i in range(num):
        for x in range(i + 1,num):
            if nums[i] < nums[x]:
                nums[i], nums[x] = nums[x], nums[i] 
    return nums

def solve_tandem_bicycle():
    try:
        type = int(input())
        num = int(input())
        farmers = list(map(int,input().split()))
        city = list(map(int,input().split()))

        if type == 1:
            farmers = high_low(num,farmers)
            city = high_low(num,city)
            an = 0
            for i in range(num):
                an += max(farmers[i],city[i])
            print(an)

        elif type == 2:
            farmers = high_low(num,farmers)
            city = low_high(num,city)
            an = 0
            for i in range(num):
                an += max(farmers[i],city[i])
            print(an)
    except: pass

#solve_tandem_bicycle()

# ===============================================================
# CCC 2022 Senior 2: Good Groups
# Link: https://cemc.uwaterloo.ca/contests/computing/2022/ccc/senior/enunciados.pdf
# ===============================================================

def solve_good_groups():
    try:
        n = int(input())
        must = [input().split() for _ in range(n)]
        a = int(input())
        cannot = [input().split() for _ in range(a)]
        c = int(input())
        group = [input().split() for _ in range(c)]

        group_of = {}

        for gid, members in enumerate(group):
            for name in members:
                group_of[name] = gid

        violations = 0

        for pair in must:
            a = pair[0]
            b = pair[1]
            if group_of[a] != group_of[b]:
                violations  = violations + 1

        for pair in cannot:
            a = pair[0]
            b = pair[1]
            if group_of[a] == group_of[b]:
                violations = violations + 1

        print(violations)
    except: pass

#solve_good_groups()

# =====================================================
# CCC 2012 - Senior 5 / Junior 5
# Problem: Mouse Journey
# Link: https://dmoj.ca/problem/ccc12s3
# =====================================================

def solve_mouse_journey():
    try:
        R = int(input())         
        C = int(input())          
        grid = [list(input().strip()) for _ in range(R)]

        def count_paths(r, c):
            if r >= R or c >= C:
                return 0

            if grid[r][c] == 'X':
                return 0

            if r == R - 1 and c == C - 1:
                return 1

            right_paths = count_paths(r, c + 1)
            down_paths = count_paths(r + 1, c)
            return right_paths + down_paths

        result = count_paths(0, 0)
        print(result)
    except: pass

#solve_mouse_journey()

# ============================================================
# CCC 2021 Senior 2 — Modern Art
# Official Online Judge Link:
# https://dmoj.ca/problem/ccc21s2
# ============================================================

def solve_modern_art():
    try:
        data = sys.stdin.read().split()
        if not data: return
        R = int(data[0])
        C = int(data[1])
        N = int(data[2])
        row_flip = [0] * (R + 1)
        col_flip = [0] * (C + 1)
        idx = 3
        for _ in range(N):
            t = data[idx]
            x = int(data[idx+1])
            idx += 2

            if t == 'Row':
                row_flip[x] ^= 1
            else:
                col_flip[x] ^= 1
                
        row_odd = 0
        for r in range(1, R+1):
            if row_flip[r] == 1:
                row_odd += 1

        col_odd = 0
        for c in range(1, C+1):
            if col_flip[c] == 1:
                col_odd += 1
        black = row_odd * (C - col_odd) + col_odd * (R - row_odd)

        print(black)
    except: pass

#solve_modern_art()

# ============================================================
# CCC 2017 Senior 2 – High Tide, Low Tide
# Link : https://dmoj.ca/problem/ccc17s2
# ============================================================

def solve_high_tide_low_tide():
    try:
        num = int(input().strip())
        data = list(map(int,input().split()))
        data.sort()
        mid = (num + 1) // 2
        low_tides = data[:mid]
        high_tides = data[mid:]
        low_tides.reverse()
        result = []
        for i in range(len(high_tides)):
            result.append(low_tides[i])
            result.append(high_tides[i])
        if len(low_tides) > len(high_tides):
            result.append(low_tides[-1])
        print(*result)
    except Exception as e:
        print("Error:", e)

#solve_high_tide_low_tide()

