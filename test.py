import os
import csv
from collections import Counter
import sys
import itertools

# import pandas as pd

# with open('us_perm_visas.csv', encoding='utf-8') as csvfile:
#     reader = csv.reader(csvfile)
#     nextLine = next(reader)
#     headers = []
#     countryOfCitizenship = []
#     i = 0
#     key = ""
#     colCount = 0
#     rowCount = 0
#     for row in csvfile:
#         rowCount = rowCount + 1
#     for item in nextLine:
#         headers.append(item)
#     key = headers[10]  # Country of Citizenship
#     for col in nextLine:
#         colCount = colCount + 1
#         if col == key:
#             print(
#                 "Found")  # Instead of printing found, if col == key (country of citizenship), then print the value of this column in every row.
#     print(colCount)
#     print(rowCount)
import itertools

import pandas
import pandas as pd

#data = pd.read_csv('us_perm_visas.csv', low_memory=False, error_bad_lines=False)
data = pd.read_csv('us_perm_visas.csv', low_memory=False, error_bad_lines=False)
data_dict = {col: list(data[col]) for col in data.columns}

df = pd.DataFrame(data_dict)

csvdata = df.info(memory_usage='deep')

print(csvdata)

CountriesCount = df['country_of_citizenship'].value_counts()

# df.groupby(['country_of_citizenship'], ['case_status']).size()

# compare = pd.crosstab(df.country_of_citizenship == "INDIA", df.pw_job_title_9089 == 'Software Developers, Systems Software')

# compare = pd.crosstab(df.country_of_citizenship == "MEXICO", df.case_status == 'Denied')

#compare = pd.crosstab(df.pw_job_title_9089 == "Landscaping and Groundskeeping Workers", df.case_status)
# print(compare)
# if df['country_of_citizenship'].to_string() == "Mexico":
#    print(df['case_status'].to_string())

# print(CountriesCount)

# print(df['country_of_citizenship'].to_string(index = False))

# resultpercent = pd.crosstab(df['us_economic_sector'],df['case_status']).apply(lambda r: r/r.sum(), axis=1)
# resultEconSector = pd.crosstab(df['us_economic_sector'],df['case_status'])
# sorted_Econresultpercent = resultpercent.sort_values(by = ['Certified'], ascending=True)

'''resultCountry = pd.crosstab(df['country_of_citizenship'],df['case_status'])
resultCountrySorted = resultCountry.sort_values(by = ['Certified'], ascending=False)

resultCountryPercent = pd.crosstab(df['pw_job_title_9089'], df['case_status']).apply(lambda r: r/r.sum(), axis=1)
sorted_resultCountryPercent = resultCountryPercent.sort_values(by = ['Certified'], ascending=False)

#with pd.option_context('display.max_rows', 999):
 #   print(sorted_resultCountryPercent)

scores = []
max_points = 190
with open('CountryScores.txt', 'r') as f:
    for line in f:
        scores.append(line.split(None, 35)[0])

with open('CountrySc.txt', 'r') as a:
    with open('CountryTest.txt', 'w') as w:
        for i in itertools.islice(scores, 0, 41):
                w.write((str(i).split(None, 35)[0] + " , "))
                w.write(str(191)  + '\n')
        for i in itertools.islice(scores, 41, 192):
                print(i)
                w.write(str(i) +" , ")
                w.write(str(max_points) + '\n')
                max_points = max_points - 1
        a.close()


#with open("economic sector.txt", "r") as f:
 #   with open("EconomicSorted.txt", "w") as r:
  #      lines = f.readlines()
   #     lines.sort()
     #   for item in lines:
    #        r.write(item)

#with pd.option_context('display.max_rows', 999):
 #   print(CountriesCount)
  #  with open('Countries.txt', 'w') as a:
   #     a.write(str(CountriesCount))
    #    a.close()

#with open('CountryPoints.txt', 'r') as a:
 #   for item in a:
  #    print(item)
   # a.close()

with pd.option_context('display.max_rows', 999):
    print(sorted_resultCountryPercent)

    s = []

    for item in sorted_resultCountryPercent:
        if item not in s:
            s.append(item)

    with open('CountryPoints.txt', 'w') as a:
        max_points = len(s)
        for i in s:
            print(i)
            a.write(str(i) + '\t')

scores = []
with open('CountryScores.txt', 'r') as f:
    for line in f:
        scores.append(line.split(None, 35)[0])


with open('CountryScores.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('JobScore.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('Job', 'Score'))
        writer.writerows(lines)'''

with open('NaicsPoints.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split("	") for line in stripped if line)
    with open('Naics.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('Job', 'Score'))
        writer.writerows(lines)

#dataframe = pandas.read_csv("NaicsPoints.txt",delimiter=" ")

#dataframe.to_csv("Naics.csv", encoding='utf-8', index=False)


