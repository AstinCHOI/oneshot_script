import sys
import time


# 200 HTTP/1.1 / 1.1.1.1
# 200 HTTP/1.1 / 1.2.1.1
# 200 HTTP/1.1 / 1.1.3.1
# 200 HTTP/1.1 / 1.1.1.4
# 200 HTTP/1.1 / 1.1.1.1
# ...
# top 10 IPs
IP_INDEX = 3

def read_line(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line

def top_ips(filename):
    ip_dict = {}
    for line in read_line(filename):
        line = line.strip().split(' ')
        if line[IP_INDEX] not in ip_dict.keys():
            ip_dict[line[IP_INDEX]] = 1
        else:
            ip_dict[line[IP_INDEX]] += 1
    sorted_ip = sorted(ip_dict.items(), key=lambda x: x[1], reverse=True)
    print(sorted_ip[:10])


class Node:
    def __init__(self, ip=None, num=0, nxt=None):
        self.ip = ip
        self.num = num
        self.nxt = nxt


def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i][1] > array[begin][1]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot

def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot-1)
        _quicksort(array, pivot+1, end)

    return _quicksort(array, begin, end)

def top_ips2(filename):
    ip_dict = {}
    for line in read_line(filename):
        line = line.strip().split(' ')
        if line[IP_INDEX] not in ip_dict.keys():
            ip_dict[line[IP_INDEX]] = 1
        else:
            ip_dict[line[IP_INDEX]] += 1

    ip_list = list(ip_dict.items())
    quicksort(ip_list)
    print(ip_list[:10])


if __name__ == '__main__':
    start_time = time.time()
    top_ips(sys.argv[1]) # using import
    print("--- %s seconds ---\n" % (time.time() - start_time))

    start_time = time.time()
    top_ips2(sys.argv[1]) # using qsort
    print("--- %s seconds ---\n" % (time.time() - start_time))
