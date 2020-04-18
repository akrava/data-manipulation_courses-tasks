import MapReduce
import sys

mr = MapReduce.MapReduce()


def mapper(record):
    id_str = record[0]
    nucleotides = record[1]
    payload = nucleotides[:-10]
    mr.emit_intermediate(len(payload), payload)


def reducer(_key, list_of_values):
    nucleotides = set()
    for x in list_of_values:
        nucleotides.add(x)
    for x in nucleotides:
        mr.emit(x)


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
