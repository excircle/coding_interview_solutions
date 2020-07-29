from typing import List

def twoSum(l: List[int], t: int) -> List[int]:
	result = []
	for v in l:
		if v > 9:
			l.remove(v)
	for key, _ in enumerate(l):
		for k, _ in enumerate(l):
			trial = l[key:k+1]
			validate = sum(trial)
			if validate == 9:
				result.append(trial)
				break
	return result

tl = [2, 7, 11, 15]
target = 9

print(twoSum(tl, target))