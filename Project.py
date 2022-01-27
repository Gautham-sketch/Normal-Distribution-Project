import statistics
import plotly.figure_factory as ff
import pandas as pd

reader = pd.read_csv("StudentsPerfomance.csv")
data = reader["lunch"].to_list()

mean = statistics.mean(data)
mode = statistics.mode(data)
median = statistics.median(data)
stdev = statistics.stdev(data)

first_std_deviation_start , first_std_deviation_end = mean - stdev , mean + stdev
second_std_deviation_start , second_std_deviation_end = mean - (2*stdev) , mean + (2*stdev)
third_std_deviation_start , third_std_deviation_end = mean - (3*stdev) , mean + (3*stdev)

thin_1_std_deviation = [result for result in data if result > first_std_deviation_start and result < first_std_deviation_end]
thin_2_std_devistion = [result for result in data if result > second_std_deviation_start and result < second_std_deviation_end]
thin_3_std_devistion = [result for result in data if result > third_std_deviation_start and result < third_std_deviation_end]

final_result = []

probablity = len(final_result)*100/len(data)
print("{} percentage of data lies in the range".format(probablity))