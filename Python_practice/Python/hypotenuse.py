def hypotenuse(s1, s2):
	sq_s1 = s1**2
	sq_s2 = s2**2
	sum_sqs = sq_s1+sq_s2
	result = (sum_sqs)**0.5
	return result

print hypotenuse(3, 4)
