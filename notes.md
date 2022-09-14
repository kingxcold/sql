Try to make the update fast as possible
updating 400 tracks (rows) and each track have 20 col (columns)


test in terms of performance first and readability second

ROW BY ROW = 0.688, 0.720, 0.665 ---> average (0.691)

ON_DUPLICATE = 0.047, 0.023, 0.031 ---> average(0.033) 21x faster than "ROW BY ROW" and 1.8x faster than "CASE"

CASE = 0.065, 0.058, 0.062 ---> average (0.061) 11x faster than ROW BY ROW
