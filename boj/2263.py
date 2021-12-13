import sys
sys.setrecursionlimit(100000)

n = int(sys.stdin.readline().strip())
in_order = list(map(int,sys.stdin.readline().split()))
post_order = list(map(int,sys.stdin.readline().split()))

def to_preorder(in_start,in_end,post_start,post_end):
    if in_start > in_end or post_start > post_end:
        return
    elif in_start == in_end:
        print(in_order[in_start], end=" ")
        return
    
    root = post_order[post_end]
    print(root, end=" ")

    left_count = in_order.index(root, in_start, in_end+1) - in_start

    to_preorder(in_start,in_start+left_count-1,post_start,post_start+left_count-1)
    to_preorder(in_start+left_count+1,in_end,post_start+left_count,post_end-1)

to_preorder(0, len(in_order)-1, 0, len(post_order)-1)