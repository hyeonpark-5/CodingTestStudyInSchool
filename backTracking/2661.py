#2661 좋은 수열


#숫자는 오직 1, 2, 3
# 현재가 앞이랑 같으면 안됨
# 숫자 체크해야될 듯

#반 나눠서 같으면 안됨 그럼 홀수면 어떻게 할건데


# 나쁜 수열인지 확인
# 임의의 길이의 인접한 두 개의 부분 수열이 동일한 것이 있으면 안됨
# def bad(arr){
#     #문자열 받아서 검사해보기
    
#     return array

# }


#abab이면 어떻게 할 것인가?





def dfs(x, res):
    global answer
    # if # 나쁜 수열인 지 확인 (가지치기)
    # 나쁜 수열이면 return
    if x == n:

        # 만약에 나쁜 수열이 아니면 
        # 단 최초의 수열만 배열로 해서 할지 정하삼 
        # 만약에 배열이면 길이가 1 이상이면 return 하는 가지치기

        answer.append(res)
        return 
    

    for i in (1, 2, 3):
        res += i
        dfs(x + 1, res)
        res = res[:-1]




n = int(input())
res = ""
answer = []
check = {}
dfs(0, res)

# 문자열로 합치는게 좋을 듯


#첫번째로 찾은 수를 반환하면 됨

#어떻게 나쁜 수열인지 확인할 것인가?


