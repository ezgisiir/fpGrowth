from fpTree import Tree, ConditionalPatternBase
import pandas as pd
from functools import reduce
#from datetime import datetime
import time

#dt = datetime.now()

#start = dt.microsecond
#start=time.time()

dataSet = './adult.data'
#dataSet = './sikko.data'
#dataSet = './adult-min.data'
df = pd.read_csv(dataSet, header=None)

for minval in (1.3024, 3.256, 162.8, 325.6, 651.2, 1628, 3256, 6512, 16280, 19536):
    minSupport = minval
    colCount = df.shape[1]
    print('Running with min support:', minSupport)
    start = time.time()
    tree = Tree()
    unique_values = set()
    unique_value_conditional_pattern_bases = dict()

    for index, row in df.iterrows():
        row_words = []
        for i in range(colCount):
            val = row[i]
            if not pd.isna(df.iloc[index, i]):
                unique_values.add(val)
                row_words.append(val)
        tree.add_words(row_words)

    for unique_value in unique_values:
        conditional_pattern_base_list = tree.get_conditional_pattern_base(unique_value)
        unique_value_conditional_pattern_bases[unique_value] = conditional_pattern_base_list

    for unique_value in unique_values:
        list_of_word_list = []
        conditional_pattern_base_list = unique_value_conditional_pattern_bases[unique_value]
        res_freq = 0
        for conditional_pattern_base in conditional_pattern_base_list:
            list_of_word_list.append(conditional_pattern_base.get_words())
            res_freq = res_freq + conditional_pattern_base.freq

        if res_freq > minSupport and len(list_of_word_list) > 0:
            res = list(reduce(lambda i2, j: i2 & j, (set(x) for x in list_of_word_list)))
            if len(res) > 0:
                print(res, res_freq)

    #dt = datetime.now()

    end = time.time()

    difference = end - start

    print('Run time:', difference, ' seconds.', 'Support:', minSupport)