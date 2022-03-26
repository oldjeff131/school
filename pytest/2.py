def sum(n1, n2):
	return n1+n2

def test_sum_int():
	assert sum(1,2) == 3

def test_sum_str():
	assert sum('1', '2') =='12'