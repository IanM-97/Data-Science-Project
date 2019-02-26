import os
import csv
from collections import Counter
import sys
import pandas as pd

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

#     key = headers[10]  # Country of Citizenship
#     for col in nextLine:
#         colCount = colCount + 1
#         if col == key:
#             print(
#                 "Found")  # Instead of printing found, if col == key (country of citizenship), then print the value of this column in every row.
#     print(colCount)
#     print(rowCount)

# data = pd.read_csv('us_perm_visas.csv', low_memory=False, error_bad_lines=False)
# data_dict = {col: list(data[col]) for col in data.columns}
#
# df = pd.DataFrame(data_dict)
#
# csvdata = df.info(memory_usage='deep')
#
# #print(csvdata)
#
# CountriesCount = df['country_of_citizenship'].value_counts()

# df.groupby(['country_of_citizenship'], ['case_status']).size()

# compare = pd.crosstab(df.country_of_citizenship == "INDIA", df.pw_job_title_9089 == 'Software Developers, Systems Software')

# compare = pd.crosstab(df.country_of_citizenship == "MEXICO", df.case_status == 'Denied')

#compare = pd.crosstab(df.pw_job_title_9089 == "Landscaping and Groundskeeping Workers", df.case_status)
# print(compare)
# if df['country_of_citizenship'].to_string() == "Mexico":
#    print(df['case_status'].to_string())

# print(CountriesCount)

# print(df['country_of_citizenship'].to_string(index = False))
#
# resultpercent = pd.crosstab(df['us_economic_sector'],df['case_status']).apply(lambda r: r/r.sum(), axis=1)
# resultEconSector = pd.crosstab(df['us_economic_sector'],df['case_status'])
# sorted_Econresultpercent = resultpercent.sort_values(by = ['Certified'], ascending=False)
#
# resultCountryPercent = pd.crosstab(df['country_of_citizenship'], df['case_status']).apply(lambda r: r/r.sum(), axis=1)
# resultCountry = pd.crosstab(df['country_of_citizenship'],df['case_status'])
# sorted_resultCountry = resultCountryPercent.sort_values(by = ['Certified'], ascending=False)
#
# print(sorted_Econresultpercent)

#sorted_Econresultpercent = sorted_Econresultpercent.astype(str)

# text_file = open("economic sector.txt", "w")
# text_file.write(str(sorted_Econresultpercent))
# text_file.close()

with open('economic sector.txt', encoding='utf-8') as f:
    rows = []
    text_file2 = open('sector_points.txt', encoding='utf-8')
    for item in f:
        rows.append(item)

    max_points = len(rows)
    for i in range(0, len(rows)):
        rows[i] = max_points
        max_points = max_points - 1

        #text_file2.write(str(i))
        print(rows[i])

    text_file2.close()
