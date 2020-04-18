import MapReduce
import sys

mr = MapReduce.MapReduce()


def mapper(record):
    person = record[0]
    friend = record[1]
    mr.emit_intermediate(person, friend)
    mr.emit_intermediate(friend, person)


def reducer(key, list_of_values):
    friends = set()
    for x in list_of_values:
        if x in friends:
            friends.remove(x)
        else:
            friends.add(x)
    for x in friends:
        mr.emit((key, x))


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
