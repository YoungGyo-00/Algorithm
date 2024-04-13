n = int(input())
group = list(map(int, input().split()))
b, c = map(int, input().split())


def solution():
    cnt = 0

    for members in group:
        members -= b
        cnt += 1
        if members > 0:
            cnt = cnt + (members // c)
            if members % c:
                cnt += 1
    return cnt


print(solution())
