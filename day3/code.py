import re
from intervaltree import IntervalTree

def read_input():
	with open('input.txt') as f:
		content = f.read()

	return content.split('\n')

def process_content_into_intervals(content):
	x_interval = IntervalTree()
	y_interval = IntervalTree()
	for line in content:
		m = re.search('#(\d{1,4}) @ (\d{1,4}),(\d{1,4}): (\d{1,4})x(\d{1,4})', line)
		
		if m:
			x_i = int(m.group(2))
			y_i = int(m.group(3))
			x_f = x_i + int(m.group(4))
			y_f = y_i + int(m.group(5))
		
			x_interval[x_i:x_f] = m.group(1)
			y_interval[y_i:y_f] = m.group(1)

	return (x_interval, y_interval)	

def find_overlapping_area(x_interval, y_interval):
	area = 0
	for x in range(0,999):
		allgroupsinx = {i.data for i in x_interval[x]}
		# print (allgroupsinx)
		for y in range(0,999):
			allgroupsiny = {i.data for i in y_interval[y]}
			inter = allgroupsinx & allgroupsiny
			if len(inter) > 1:
				area = area + 1
		
	return area
					
if __name__ == '__main__':
	content = read_input()
	(x_interval, y_interval) = process_content_into_intervals(content)
	area = find_overlapping_area(x_interval, y_interval)
	print(area)