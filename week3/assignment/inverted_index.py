import MapReduce
import sys

mr = MapReduce.MapReduce()


def mapper(record):
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
        mr.emit_intermediate(w, key)


def reducer(key, list_of_values):
    documents = set()
    for v in list_of_values:
        documents.add(v)
    mr.emit((key, list(documents)))


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
