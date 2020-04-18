import MapReduce
import sys

mr = MapReduce.MapReduce()
max_rows = 5
max_columns = 5
mr.should_sort = True


def mapper(record):
    matrix = record[0]
    i = record[1]
    j = record[2]
    value = record[3]
    for k in range(max_columns if matrix == 'a' else max_rows):
        if matrix == 'a':
            indexes = (i, k)
        else:
            indexes = (k, j)
        mr.emit_intermediate(indexes, record)


def reducer(key, list_of_values):
    n = max(max_rows, max_columns)
    row = [0] * n
    column = [0] * n
    for x in list_of_values:
        matrix = x[0]
        i = x[1]
        j = x[2]
        value = x[3]
        target = row if matrix == 'a' else column
        target[j if matrix == 'a' else i] = value
    result = 0
    for k in range(n):
        result += row[k] * column[k]
    if result != 0:
        mr.emit(key + (result, ))


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
