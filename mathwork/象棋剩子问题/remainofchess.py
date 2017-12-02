import numpy as np
import math

def search_right(a,i):
	j = 0
	t = i
	while j<2 and i+1 < len(a):
		if a[i+1] != 0:
			j+=1
		i+=1
	if j == 2:
		a[t] = 0
		return a,i
	else:
		return a,-1

def search_left(a,i):
	j = 0
	t = i
	while j<2 and i-1 > -1:
		if a[i-1] != 0:
			j+=1
		i-=1
	if j == 2:
		a[t] = 0
		return a,i
	else:
		return a,-1


def right(a,i):
	is_found = 1
	old_a = a.copy()
	while i != -1:
		_i = i
		a,i = search_right(a,i)
	new_a = a.copy()
	if np.array_equal(old_a,new_a):
		is_found = 0
	return a,_i,is_found


def left(a,i):
	is_found = 1
	old_a = a.copy()
	while i != -1:
		_i = i
		a,i = search_left(a,i)
	new_a = a.copy()
	if np.array_equal(old_a,new_a):
		is_found = 0
	return a,_i,is_found


def get_result(x,y):
	min_left = x*y
	graph = np.full((x,y),1)
	if x>2 or y>2:
		for i_index in range(x):
			for j_index in range(y):
				i = i_index
				j = j_index
				a = np.copy(graph)
				while(1):
					a[i,:],j,right_is_found = right(a[i,:],j)
					a[i,:],j,left_is_found = left(a[i,:],j)
					a[:,j],i,up_is_found = left(a[:,j],i)
					a[:,j],i,down_is_found = right(a[:,j],i)
					if right_is_found == 0 and left_is_found == 0 and up_is_found == 0 and down_is_found == 0:
						break
				if a.sum() < min_left:
					min_left = a.sum()
					b = a.copy()
					i_ = i_index
					j_ = j_index
	else:
		min_left = graph.sum()
		b = np.copy(graph)
		i_ = 1
		j_ = 1
	return min_left,b, i_, j_

dic = {}
for x in range(3,10):
	for y in range(3,10):
		xy_max = max(x,y)
		xy_min = min(x,y)
		min_left,b,i_,j_ = get_result(x,y)
		if min_left < dic.get((xy_min,xy_max),float('inf')):
			dic[(xy_min,xy_max)] = min_left
dic = sorted(dic.items(), key=lambda d:d[0])
print(dic) 

			
