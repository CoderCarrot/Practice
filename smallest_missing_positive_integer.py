def solution(A):

    A.sort()
    count = 0
    start = 1

    for num in A:
        if num <= 0:
            count += 1
        elif num >1:
            break
        else:
            start = num + 1
            nums = set(A[count:])
            while start in nums:
                start += 1
            break

    return start
