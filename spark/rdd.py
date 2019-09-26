import math

from pyspark import SparkContext

sc = SparkContext()

yeet = [2.3, 3.4, 4.4, 2.4, 3.3, 4.0]

# Parallelize the list, yeet
parallel_yeet = sc.parallelize(yeet, 2)

# Collect all of the yeets
print(parallel_yeet.collect())

# Take two elements from the list
print(parallel_yeet.take(2))

# Get the number of partitions
print(parallel_yeet.getNumPartitions())

temp_data = [59, 58, 34, 43, 23, 42]

parallel_temp_data = sc.parallelize(temp_data, 2)

print(parallel_temp_data.collect())


def f(ls):
    s = 0
    for i in ls:
        if (i * 2) % 4 == 0:
            s += i * 2
    return math.sqrt(s)


def f(ls):
    s = 0
    for i in ls:
        if (i * 2) % 4 == 0:
            s += i * 2
    return math.sqrt(s)


print(f(range(100000)))

values = sc.parallelize(range(100000))

new = lambda x, y: x + (y * 2)
print(math.sqrt(values.filter(lambda x: (x * 2) % 4 == 0).reduce(new)))

print(
    math.sqrt(
        values.map(lambda n: n * 2)
        .filter(lambda n: n % 4 == 0)
        .reduce(lambda a, b: a + b if b % 4 == 0 else a)
    )
)
