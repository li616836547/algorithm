# _*_ encoding utf-8 _*_
# Li Hanpeng 12-14


# 冒泡排序算法
def bubble(the_list):
    n = len(the_list)
    for i in range(n-1):
        for j in range(n-i-1):
            if the_list[j] > the_list[j+1]:
                q = the_list[j]
                the_list[j] = the_list[j+1]
                the_list[j+1] = q
    return the_list


# 快速排序
def quick_sort(l, left, right):
    low = left
    high = right
    key = l[low]
    if low > high:
        return l
    while low < high:
        while (low < high) and (l[high] >= key):
            high = high - 1
        l[low] = l[high]
        while (low < high) and (l[low] <= key):
            low = low + 1
        l[high] = l[low]
    l[low] = key
    quick_sort(l, left, low-1)
    quick_sort(l, low+1, high)
    return l









# 主函数
if __name__ == '__main__':
    l = [1,3,6,3,3,2,45,2.5]
    print(bubble(l))
    print(quick_sort(l, 0, len(l)-1))
