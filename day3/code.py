import re
import intervaltree

def read_input():
	with open('input.txt') as f:
		content = f.read()
	return content

def process_content_into_intervals(content):
	x_intervals = IntervalTree()
	y_intervals = IntervalTree()
	for line in content:
		m = re.search('(\d{1,4}),(\d{1,4}): (\d{1,4})x(\d{1,4})', line)
		
		x_i = int(m.group(1))
		y_i = int(m.group(2))
		x_f = x_i + int(m.group(3))
		y_f = y_i + int(m.group(4))
		
		x_interval[x_i:x_f] = 1
		y_interval[y_i:y_f] = 1

	return (x_interval, y_interval)	

if __name__ == '__main__':
	content = read_input()
	process_content_into_intervals(content)		