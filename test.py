import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv
df = pd.read_csv('studentMarks.csv')
data = df['Math_score'].tolist()
#fig = ff.create_distplot([data], ['math Score'], show_hist = False)
#fig.show()
#mean and standard deviation for calculating the z-test as z-score=(sample mean-mean)/standard deviation
mean = statistics.mean(data)
print("this is the mean of population : ", mean)
std_deviation = statistics.stdev(data)
print('this is the std deviation of population: ', std_deviation)
##  code to find the mean of 100 data points 1000 times 
#function to get the mean of the given data samples
# pass the number of data points you want  as counter
def random_set_of_mean(counter):
    data_set = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        data_set.append(value)
    mean = statistics.mean(data_set)
    return mean

#Pass the number of time you want the mean of the data points as a parameter in range function in for loop
mean_list = []
for i in range(0,1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)
# calculating mean and standard_deviation of the sampling distribution.
standard_deviation = statistics.stdev(mean_list)
print('std dev of sample data : ', standard_deviation)
mean = statistics.mean(mean_list)
print("mean of sampling distribution:- ",mean)

#finding standard deviation starting and ending values
first_std_dev_start, first_std_dev_end = mean-std_deviation, mean+std_deviation
second_std_dev_start, second_std_dev_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_dev_start, third_std_dev_end = mean-(3*std_deviation), mean+(3*std_deviation)
print("first std dev : ", first_std_dev_start, first_std_dev_end)
print("second std dev : ", second_std_dev_start, second_std_dev_end)
print("third std dev", third_std_dev_start, third_std_dev_end)

