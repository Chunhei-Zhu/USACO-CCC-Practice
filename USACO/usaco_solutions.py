import sys
from itertools import permutations

# =============================================================================
# USACO Solutions
# =============================================================================

# ================================
# USACO Bronze: Blocked Billboard
# Link: https://usaco.org/index.php?cpid=759&page=viewproblem2
# ================================

def _area(rect):
    x1, y1, x2, y2 = rect
    w = max(0, x2 - x1)
    h = max(0, y2 - y1)
    return w * h

def _overlap(a, b):
    ax1, ay1, ax2, ay2 = a
    bx1, by1, bx2, by2 = b
    w = max(0, min(ax2, bx2) - max(ax1, bx1))
    h = max(0, min(ay2, by2) - max(ay1, by1))
    return w * h

def solve_blocked_billboard():
    print('Enter Test Data To 1.Blocked Billboard')
    try:
        data = sys.stdin.read().split()
        if not data: return
        ax1, ay1, ax2, ay2 = map(int, data[0:4])
        bx1, by1, bx2, by2 = map(int, data[4:8])
        tx1, ty1, tx2, ty2 = map(int, data[8:12])

        A = (ax1, ay1, ax2, ay2)
        B = (bx1, by1, bx2, by2)
        T = (tx1, ty1, tx2, ty2)

        visible_A = _area(A) - _overlap(A, T)
        visible_B = _area(B) - _overlap(B, T)

        print(visible_A + visible_B)
    except: pass


# ================================
# USACO Bronze: Rectangle Pasture
# ================================

def solve_rectangle_pasture():
    print('Enter Test Data To 2.Rectangle Pasture')
    try:
        data = sys.stdin.read().split()
        if not data: return
        n = int(data[0])
        coords = list(map(int, data[1:]))
        
        allx = []
        ally = []
        for i in range(0, len(coords), 2):
            allx.append(coords[i])
            ally.append(coords[i+1])
            
        minx = min(allx)
        maxx = max(allx)
        miny = min(ally)
        maxy = max(ally)
        area = (maxx - minx) * (maxy - miny)
        print(area)
    except: pass


# ================================
# USACO Bronze: Cow Gymnastics
# Link: https://usaco.org/index.php?cpid=963&page=viewproblem2
# ================================

def always_before(i, j, pos, K):
    for r in range(K):
        if pos[r][i] >= pos[r][j]:
            return False
    return True

def solve_cow_gymnastics():
    print('Enter Test Data To 3.Cow Gymnastics')
    try:
        data = sys.stdin.read().split()
        if not data: return
        
        K = int(data[0])
        N = int(data[1])
        
        pos = []
        idx = 2
        for _ in range(K):
            rank = list(map(int, data[idx:idx+N]))
            idx += N
            one_race_pos = {}
            for index, cow in enumerate(rank):
                one_race_pos[cow] = index
            pos.append(one_race_pos)
            
        ans = 0
        for i in range(1, N+1):
            for j in range(1, N+1):
                if i == j:
                    continue
                if always_before(i, j, pos, K):
                    ans += 1
        print(ans)
    except: pass


# ================================
# USACO Bronze: Mixing Milk
# Link: https://usaco.org/index.php?cpid=855&page=viewproblem2
# ================================

def mixing_ops(a, ah, b, bh, c, ch):
    step = 0
    while step < 100:
        if bh + ah <= b:
            bh = bh + ah
            ah = 0
        else:
            ah = bh + ah - b
            bh = b
        step += 1
        if step == 100: break

        if ch + bh <= c:
            ch = ch + bh
            bh = 0
        else:
            bh = ch + bh - c
            ch = c
        step += 1
        if step == 100: break

        if ah + ch <= a:
            ah = ah + ch
            ch = 0
        else:
            ch = ah + ch - a
            ah = a
        step += 1

    print(ah)
    print(bh)
    print(ch)

def solve_mixing_milk():
    print('Enter Test Data To 4.Mixing Milk')
    try:
        data = sys.stdin.read().split()
        if not data: return
        a, ah = int(data[0]), int(data[1])
        b, bh = int(data[2]), int(data[3])
        c, ch = int(data[4]), int(data[5])
        mixing_ops(a, ah, b, bh, c, ch)
    except: pass


# ================================
# USACO Bronze: Bucket Brigade
# Link: https://usaco.org/index.php?cpid=939&page=viewproblem2
# ================================

def other_bb(barn, lake): 
    maxabsx = max(barn[0], lake[0])
    minabsx = min(barn[0], lake[0])
    maxabsy = max(barn[1], lake[1])
    minabsy = min(barn[1], lake[1])
    an = (maxabsx - minabsx) + (maxabsy - minabsy) - 1
    return an

def lakex_barnx_rockx(barn, lake, rock):
    if barn[0] == lake[0] and lake[0] == rock[0] and max(barn[1], lake[1]) > rock[1] > min(barn[1], lake[1]):
        maxan = max(barn[1], lake[1])
        minan = min(barn[1], lake[1])
        an = maxan - minan + 1
    else:
        maxan = max(barn[1], lake[1])
        minan = min(barn[1], lake[1])
        an = maxan - minan - 1
    return an

def lakey_barny_rocky(barn, lake, rock):
    if barn[1] == lake[1] and lake[1] == rock[1] and max(barn[0], lake[0]) > rock[0] > min(barn[0], lake[0]):
        maxan = max(barn[0], lake[0])
        minan = min(barn[0], lake[0])
        an = maxan - minan + 1
    else:
        maxan = max(barn[0], lake[0])
        minan = min(barn[0], lake[0])
        an = maxan - minan - 1
    return an

def solve_bucket_brigade():
    print('Enter Test Data To 5.Bucket Brigade')
    try:
        data = sys.stdin.read().split()
        if not data: return
        grid = data 
        rock = None
        barn = None
        lake = None
        
        for y in range(10):         
            for x in range(10):     
                if grid[y][x] == 'B':
                    barn = (x, y)   
                if grid[y][x] == 'L':
                    lake = (x, y)   
                if grid[y][x] == 'R':
                    rock = (x, y)  

        if rock is not None and barn[0] == lake[0] and lake[0] == rock[0] and max(barn[1], lake[1]) > rock[1] > min(barn[1], lake[1]):
            print(lakex_barnx_rockx(barn, lake, rock))
        elif rock is not None and barn[1] == lake[1] and lake[1] == rock[1] and max(barn[0], lake[0]) > rock[0] > min(barn[0], lake[0]):
            print(lakey_barny_rocky(barn, lake, rock))
        else:
            print(other_bb(barn, lake))
    except: pass


# ================================
# Codeforces 1133C – Balanced Team
# ================================

def low_high_nums(num,nums):
    for a in range(num):
        for b in range(num-1):
            if nums[b] > nums[b+1]:
                nums[b],nums[b+1] = nums[b+1],nums[b]
    return nums

def found(num,nums):
    l = 0
    ans = 0
    newnums = low_high_nums(num,nums)
    for i in range(num):
        while newnums[i] - newnums[l] > 5:
                l += 1
        ans = max(ans,i - l + 1)
    return ans

def solve_balanced_teams():
    print('Enter Test Data To 7.Balanced Teams')
    try:
        data = sys.stdin.read().split()
        if not data: return
        num = int(data[0])
        nums = list(map(int, data[1:]))
        an = found(num,nums)
        print(an)
    except: pass


# ================================
# USACO Bronze: Shell Game
# Link: https://usaco.org/index.php?page=viewproblem2&cpid=891
# ================================

def solve_shell_game():
    print('Enter Test Data To 12.Shell Game')
    try:
        data = sys.stdin.read().split()
        if not data: return
        num = int(data[0])
        
        ops = []
        idx = 1
        for _ in range(num):
            ops.append(list(map(int, data[idx:idx+3])))
            idx += 3
            
        an = 0
        for start in [1,2,3]:
            pearl = start
            correct = 0
            for a,b,g in ops:
                if pearl == a:
                    pearl = b
                elif pearl == b:
                    pearl = a
                if pearl == g:
                    correct += 1
            an = max(correct,an)
        print(an)
    except: pass


# ================================================
# USACO 2024 January Contest, Bronze Division: Cow College
# Link: https://usaco.org/index.php?page=viewproblem2&cpid=1377
# ================================================

def solve_cow_college():
    print('Enter Test Data To 13.Cow College')
    try:
        data = sys.stdin.read().split()
        if not data: return
        num = int(data[0])
        nums = [int(x) for x in data[1:]]
        
        result = 0
        an = 0
        ans = 0
        for i in range(num):
            bigger = 0
            for j in range(num):
                if nums[j] >= nums[i]:
                    bigger += 1
            newresult = nums[i] * bigger
            if newresult > result:
                result = newresult
                an = nums[i]
                ans = newresult
        print(an,ans)
    except: pass


# ===========================================
# USACO Bronze 2019 US Open – Problem: The Bucket Brigade
# Link: https://usaco.org/index.php?page=viewproblem2&cpid=939
# ===========================================

def bucket_x_to_fire_x(bucket,fire,rock):
    if bucket[1] == fire[1] and bucket[1] == rock[1] and max(bucket[0],fire[0]) > rock[0] > min(bucket[0],fire[0]):
        an = max(bucket[0],fire[0]) - min(bucket[0],fire[0]) + 1
    else:
        an = max(bucket[0],fire[0]) - min(bucket[0],fire[0]) - 1
    return an

def bucket_y_to_fire_y(bucket,fire,rock):
    if bucket[0] == fire[0] and bucket[0] == rock[0] and max(bucket[1],fire[1]) > rock[1] > min(bucket[1],fire[1]):
        an = max(bucket[1],fire[1]) - min(bucket[1],fire[1]) + 1
    else:
        an = max(bucket[1],fire[1]) - min(bucket[1],fire[1]) -1
    return an

def other_simple(bucket,fire):
    X = max(bucket[0],fire[0]) - min(bucket[0],fire[0])
    Y = max(bucket[1],fire[1]) - min(bucket[1],fire[1])
    an = X + Y - 1
    return an 

def solve_the_bucket_brigade():
    try:
        farm = sys.stdin.read().split()
        if not farm: return
        print('')
        rock = None

        for y in range(10):
            for x in range(10):
                if farm[y][x] == 'B':
                    bucket = (x,y)
                elif farm[y][x] == 'L':
                    fire = (x,y)
                elif farm[y][x] == 'R':
                    rock = (x,y)

        if rock is not None and bucket[1] == fire[1] and bucket[1] == rock[1]:
            print(bucket_x_to_fire_x(bucket,fire,rock))
        
        elif rock is not None and bucket[0] == fire[0] and bucket[0] == rock[0]:
            print(bucket_y_to_fire_y(bucket,fire,rock))
        
        else:
            print(other_simple(bucket,fire))
    except: pass


# =====================================================
# USACO Bronze: The Lost Cow
# Official problem link: https://usaco.org/index.php?page=viewproblem2&cpid=735
# =====================================================

def solve_the_lost_cow():
    try:
        data = sys.stdin.read().split()
        if not data: return
        x, y = int(data[0]), int(data[1])

        current_position = x
        step = 1
        direction = 1
        total_distance = 0

        while True:
            next_position = x + direction * step

            if (current_position <= y <= next_position) or (next_position <= y <= current_position):
                total_distance += abs(y - current_position)
                print(total_distance)
                return

            distance_this_leg = abs(next_position - current_position)
            total_distance += distance_this_leg
            current_position = next_position
            direction *= -1
            step *= 2
    except: pass


# =====================================================
# USACO Bronze: Don't Be Last!
# Official link: https://usaco.org/index.php?page=viewproblem2&cpid=712
# =====================================================

def solve_dont_be_last():
    try:
        data = sys.stdin.read().split()
        if not data: return
        n = int(data[0])
        cow = {}

        idx = 1
        for _ in range(n):
            name = data[idx]
            milk = int(data[idx+1])
            idx += 2
            cow[name] = cow.get(name, 0) + milk

        sorted_cow = sorted(cow.items(), key=lambda x: x[1])
        values = [v for _, v in sorted_cow]

        if len(values) < 2:
            print("Tie")
            return

        min_value = values[0]

        if values.count(min_value) > 1:
            print("Tie")
            return

        second_value = None
        for v in values:
            if v > min_value:
                second_value = v
                break

        if second_value is None:
            print("Tie")
            return

        if values.count(second_value) > 1:
            print("Tie")
            return

        for name, milk in sorted_cow:
            if milk == second_value:
                print(name)
                return
    except: pass


# =====================================================
# USACO Bronze: Herdle
# Problem Link: https://usaco.org/index.php?page=viewproblem2&cpid=1155
# =====================================================

def solve_herdle():
    try:
        data = sys.stdin.read().split()
        if not data: return

        guess = data[0:3]
        an = data[3:6]
        
        green = 0
        cnt_guess = [0] * 26
        cnt_an = [0] * 26
        for y in range(3):
            for x in range(3):
                if guess[y][x] == an[y][x]:
                    green += 1
                else:
                    g = ord(guess[y][x]) - ord('A')
                    a = ord(an[y][x])- ord('A')
                    cnt_guess[g] += 1
                    cnt_an[a] += 1
        yellow = 0
        for i in range(26):
            yellow += min(cnt_guess[i],cnt_an[i])
        print(green)
        print(yellow)
    except: pass


# ==========================================================================================
# USACO Bronze: Cow College Review
# Official link: https://usaco.org/index.php?page=viewproblem2&cpid=1258
# ==========================================================================================

def solve_cow_college_review():
    try:
        data = sys.stdin.read().split()
        if not data: return
        num = int(data[0])
        nums = [int(x) for x in data[1:]]
        all = 0
        maxan = 0
        for i in range(num):
            cow = 0
            for y in range(num):
                if nums[i] <= nums[y]:
                    cow += 1
            newall = nums[i] * cow
            if newall > all or (newall == all and nums[i] < maxan):
                all = newall
                maxan = nums[i]
        print(maxan,all)
    except: pass


# ============================================================
# USACO Bronze – Speeding Ticket
# Official Link: https://usaco.org/index.php?page=viewproblem2&cpid=567
# ============================================================

def solve_speeding_ticket():
    try:
        data = sys.stdin.read().split()
        if not data: return
        N = int(data[0])
        M = int(data[1])
        idx = 2
        road = []
        
        for _ in range(N):
            length = int(data[idx])
            speed = int(data[idx+1])
            road += [speed] * int(length)
            idx += 2
        bessie = []
        
        for _ in range(M):
            length = int(data[idx])
            speed = int(data[idx+1])
            bessie += [speed] * int(length)
            idx += 2
        max_over = 0
        
        for i in range(100):
            mspeed = int(road[i])
            bspeed = int(bessie[i])
            if mspeed < bspeed:
                over = bspeed - mspeed
                max_over = max(max_over,over)
        print(max_over)
    except: pass


# ============================================================
# USACO Bronze 2019 December – Livestock Lineup
# Link: https://usaco.org/index.php?page=viewproblem2&cpid=965
# ============================================================

def solve_livestock_lineup():
    print('Enter Test Data To 25.Livestock Lineup')
    try:
        cows = sorted([
            "Beatrice", "Belinda", "Bella", "Bessie", 
            "Betsy", "Blue", "Buttercup", "Sue"
        ])
        data = sys.stdin.read().split()
        if not data: return
        N = int(data[0])
        constraints = []
        idx = 1
        for _ in range(N):
            cowA = data[idx]
            cowB = data[idx + 5]
            constraints.append((cowA,cowB))
            idx += 6
        for p in permutations(cows):
            all_ok = True
            for name1,name2 in constraints:
                try:
                    idx1 = p.index(name1)
                    idx2 = p.index(name2)
                    if abs(idx1 - idx2) != 1:
                        all_ok = False
                        break
                except:
                    all_ok = False
                    break
            if all_ok:
                for cow in p:
                    print(cow)
                return
    except: pass


# ============================================================
# USACO Bronze 2020 January – Word Processor
# Link: https://usaco.org/index.php?page=viewproblem2&cpid=987
# ============================================================

def solve_word_processor():
    try:
        data  = sys.stdin.read().split()
        if len(data) < 3:
            return
        N = int(data[0])
        K = int(data[1])
        all_words = data[3:]
        
        print(data[2],end = '')
        a = len(data[2])
        
        for i in all_words:
            b = len(i)
            if (a+b) <= K:
                print(" " + i,end = '')
                a += b
            else:
                print("\n" + i,end = '')
                a = b
        print()
    except: pass

# ============================================================
# USACO 2017 December Bronze - The Bovine Shuffle
# Link: http://www.usaco.org/index.php?page=viewproblem2&cpid=760
# ============================================================

def solve_the_bovine_shuffle():
    try:
        data = sys.stdin.read().split()
        n = int(data[0])
        nums = []
        for i in range(n):
            a = int(data[i+1])
            nums.append(a-1)
        final_cows = data[n+1:]
        current_cows = final_cows
        for _ in range(3):
            past_ids = [0] * n
            for i in range(n):
                a = nums[i]
                past_ids[i] = current_cows[a]
            current_cows = past_ids
        for i in current_cows:
            print(i)

    except Exception as e:
        print("Error:", e)
#solve_the_bovine_shuffle()

# ================================
# USACO Bronze: Mixing Milk (review)
# Link: https://usaco.org/index.php?cpid=855&page=viewproblem2
# ================================

import sys
def solve_mixing_milk_review():
    data = sys.stdin.read().split()
    a = [int(data[0]),int(data[1])]
    b = [int(data[2]),int(data[3])]
    c = [int(data[4]),int(data[5])]
    all = []
    for i in range(34):
        n1 = a[1] + b[1]
        b[1] = min(b[0],n1)
        a[1] = 0
        if b[0] <= n1:
            a[1] = n1 - b[0]
            b[1] = b[0]
        if i == 33:
            break
        n2 = c[1] + b[1]
        c[1] = min(c[0],n2)
        b[1] = 0
        if c[0] <= n2:
            b[1] = n2 - c[0]
            c[1] = c[0]
        n3 = c[1] + a[1]
        a[1] = min(a[0],n3)
        c[1] = 0
        if a[0] <= n3:
            c[1] = n3 - a[0]
            a[1] = a[0]
    print(a[1])
    print(b[1])
    print(c[1])

#if __name__ == "__main__":
    #solve_mixing_milk_review()

