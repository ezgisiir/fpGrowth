from fpTree import Tree, ConditionalPatternBase
import pandas as pd
import itertools

# dataSet = './adult.data'
# dataSet = './sikko.data'
dataSet = './adult-min.data'
df = pd.read_csv(dataSet, header=None)

