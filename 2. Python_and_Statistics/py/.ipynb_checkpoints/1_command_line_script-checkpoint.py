# coding: utf-8
# Фильтрация рейтингов с оценкой 5.0

# на Mac / Linux
# cat ../data/ratings* | python ../py/1_command_line_script.py > ../data/filtered.txt

import sys

for line in sys.stdin:
	user_id, movie_id, rating, timestamp = line.strip().split(',')

	if rating == '5.0':
		print(user_id, timestamp)