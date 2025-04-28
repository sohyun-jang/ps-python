# 함수 정의를 할 때는 아직 arr라는 변수가 존재하지 않기 때문에 high = None 으로 정의
def binary_search(arr, target, low=0, high=None):
    
    # arr의 값을 안 후에, high 매개변수의 값 다시 정의하기
    if high == None:
        high = len(arr)-1
    
    # there is condition of using recursion function, try to define base case rather than using while
    if low > high:
        return -1
    
    else:
        mid = (low+high)//2
        if arr[mid] < target:
            # return is essential when using recursion function
            return binary_search(arr, target, mid+1, high)
        elif arr[mid] > target:
            # mid+1, 또는 mid-1로 새로운 매개변수 정의 해주지 않으면 무한 루프에 빠질 위험 있음
            return binary_search(arr, target, low, mid-1)
        else:
            return mid
    
        

if __name__ == "__main__":
    # test case using __name__
    n = [2, 4, 6, 8, 10, 12]
    result = binary_search(n, 8)
    print("결과: {}".format(result))