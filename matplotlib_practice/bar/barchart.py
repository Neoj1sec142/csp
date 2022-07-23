import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt


plt.style.use("fivethirtyeight")
# using Counter from collections library
# with open('data.csv') as csv_f:
#     csv_reader = csv.DictReader(csv_f)
#     c = Counter()
#     for row in csv_reader:
#         c.update(row['LanguagesWorkedWith'].split(';'))
data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_res = data['LanguagesWorkedWith']

c = Counter()
for res in lang_res:
    c.update(res.split(';'))

languages = []
pop = []

for item in c.most_common(15):
    languages.append(item[0])
    pop.append(item[1])
languages.reverse()
pop.reverse()
plt.barh(languages, pop)
# print(row['LanguagesWorkedWith'].split(';'))
plt.title("Most Popular Languages")
plt.xlabel("Number of People Using")
# plt.ylabel("Programming Languages")

plt.tight_layout()

plt.show()