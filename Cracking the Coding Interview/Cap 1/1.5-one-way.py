#!/usr/local/bin/python3

# One way


def count_changes(a, s):
	distincts = 0
	for key, _ in enumerate(a):
		if a[key] != s[key]:
			distincts += 1

	return distincts


def count_insert_del(minor, size_minor, major, size_major):
	distincts = 0
	j = 0
	for key, _ in enumerate(major):
		if j >= size_minor:
			distincts += 1
			break

		if major[key] != minor[j]:
			distincts += 1
			j -= 1

		j += 1

	return distincts


def check_on_way(a, s):
	size_a = len(a)
	size_s = len(s)
	distincts = 0
	if abs(size_a - size_s) > 1:
		return False
	elif size_a == size_s:
		distincts = count_changes(a, s)
	elif size_a > size_s:
		distincts = count_insert_del(s, size_s, a, size_a)
	else:
		distincts = count_insert_del(a, size_a, s, size_s)

	if distincts > 1:
		return False
	else:
		return True


print(check_on_way('pale', 'bake'))
