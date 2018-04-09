# DSAI_HW2-BooleanSearch

One Paragraph of project description goes here

## Project Details

To support queries of matching keywords is a “must-have” function in databases. A query term with boolean operations, such as “國際 and 籃球", is very useful to quickly identify required content in databases.
In this HW, we will give you a lot of “Chinese news titles”.  You should implement the query function to support simple boolean operations. Your query time and index time will be accumulated as your ranking.

### Pandas Read CSV

Used Pandas library to read csv file and converted to an Array

```python
# Read source csv
data = pd.read_csv(args.source, names=["index", "data"])
data = data.values
# Read query txt
queries = pd.read_csv(args.query, names=["query"])
queries = queries.values
```

### Iterate queried data

Loop thru each query and split each data 

words
Tables |
---- |
喝水 |
or |
唱歌 |

```python
for query in queries:
    tempArr = []
    operation = []
    words = query[0].split()
```

### Search and compare operators

From words, use if statement to find each operators **and**, **or**, and **not**
Use tempArr[] to compare with OptArr[] by comparing using set
After comparing both data store in tempArr and **sort**
- tempArr[] = The final result
- optArr[] = The search result from the operator

```python
for word in words:
    optArr = []
    if word == "and" or word == "or" or word == "not":
        operation = word
        continue
    if operation == "and":
        for a in tempArr:
            if word in data[a-1][1]:
                optArr.append(data[a-1][0])
        tempArr = list(set(tempArr) & set(optArr))
        continue
    if operation == "or":
        for d in data:
            if word in d[1]:
                optArr.append(d[0])
        tempArr = list(set(tempArr) | set(optArr))
        continue
    if operation == "not":
        for a in tempArr:
            if word in data[a - 1][1]:
                optArr.append(data[a - 1][0])
        tempArr = list(set(tempArr) - set(optArr))
        continue
    for d in data:
        if word not in d[1]:
            continue
        tempArr.append(d[0])
tempArr.sort()
if not tempArr:
    tempArr = list([0])
outputs.append(tempArr)
```

### Output data

By using .join operator is the easiest way to not add newline(**\n**) at the end of the file.

```python
file = open(args.output, 'w')
    for output in outputs[:-1]:
        file.write(','.join(map(str, output)))
        file.write('\n')
    else:
        file.write(','.join(map(str, outputs[-1])))
    print("--- %s seconds ---" % (time.time() - start_time))
```

## Conclusion

The project can be done by comparing data using simple operators.
This work fast enough to search 100k of data with different array.
I believe if the data size is bigger than 300k+ this will work slower than other advance methods.