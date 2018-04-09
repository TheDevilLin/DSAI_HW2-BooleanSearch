import pandas as pd
import time

if __name__ == '__main__':
    # You should not modify this part.
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--source',
                        default='source.csv',
                        help='input source data file name')
    parser.add_argument('--query',
                        default='query.txt',
                        help='query file name')
    parser.add_argument('--output',
                        default='output.txt',
                        help='output file name')
    args = parser.parse_args()


    # Please implement your algorithm below
    start_time = time.time()
    outputs = []
    
    # TODO load source data, build search engine
    data = pd.read_csv(args.source, names=["index", "data"])
    data = data.values
    # TODO compute query result
    queries = pd.read_csv(args.query, names=["query"])
    queries = queries.values
    for query in queries:
        tempArr = []
        operation = []
        words = query[0].split()
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
    # TODO output result
    file = open(args.output, 'w')
    for output in outputs[:-1]:
        file.write(','.join(map(str, output)))
        file.write('\n')
    else:
        file.write(','.join(map(str, outputs[-1])))
    print("--- %s seconds ---" % (time.time() - start_time))