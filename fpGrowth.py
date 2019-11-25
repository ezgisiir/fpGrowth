from fpTree import Tree, ConditionalPatternBase
import pandas as pd
from functools import reduce
import time

start=time.time()

#dataSet = './adult2.csv'
#dataSet = './adult3.csv'
#dataSet = './adult4.csv'
#dataSet = './adult5.csv'
#dataSet = './adult6.csv'
#dataSet = './adult7.csv'
#dataSet = './adult8.csv'
#dataSet = './adult9.csv'
#dataSet = './adult10.csv'
dataSet = './adult.data'


#dataSet = './adultap10.csv'
#dataSet = './adultap20.csv'
#dataSet = './adultap30.csv'
#dataSet = './adultap40.csv'
#dataSet = './adultap50.csv'
#dataSet = './adultap60.csv'
#dataSet = './adultap70.csv'
#dataSet = './adultap80.csv'
#dataSet = './adultap90.csv'
#dataSet = './adultap100.csv'

#dataSet = './adultp1.csv'
#dataSet = './adultp2.csv'
#dataSet = './adultp3.csv'
#dataSet = './adultp4.csv'
#dataSet = './adultp5.csv'
#dataSet = './adultp6.csv'
#dataSet = './adultp7.csv'
#dataSet = './adultp8.csv'
#dataSet = './adultp9.csv'
#dataSet = './adultp10.csv'


#dataSet = './adultt4.csv'
#dataSet = './adultt5.csv'
#dataSet = './adultt6.csv'
#dataSet = './adultt7.csv'
#dataSet = './adultt8.csv'
#dataSet = './adultt9.csv'
#dataSet = './adultt10.csv'
#dataSet = './adultt11.csv'
#dataSet = './adultt12.csv'
#dataSet = './adultt13.csv'
#dataSet = './adultt14.csv'
#dataSet = './adultt15.csv'

df = pd.read_csv(dataSet, header=None)
print(df.shape)

minSupport = 2
colCount = df.shape[1]
print('Running with min support:', minSupport)

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

#end = dt.second

difference = time.time() - start

print('Run time:', difference, ' seconds.')
