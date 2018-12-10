import csv
import numpy as np

# # import nyc_taxi.csv as a list of lists
# f = open("nyc_taxis.csv", "r")
# taxi_list = list(csv.reader(f))

# # remove the header row
# taxi_list = taxi_list[1:]

# # convert all values to floats
# converted_taxi_list = []
# for row in taxi_list:
#     converted_row = []
#     for item in row:
#         converted_row.append(float(item))
#     converted_taxi_list.append(converted_row)

# taxi = np.array(converted_taxi_list)
# taxi_ten = taxi[:10] # select ten rows

# # From the taxi ndarray:
# # - Select the row at index 0 and assign it to row_0.
# # - Select every column for the rows at indexes 391 to 500 inclusive and assign them to rows_391_to_500.
# # - Select the item at row index 21 and column index 5 and assign it to row_21_column_5

# row_0 = taxi[0] # select first row
# rows_391_to_500 = taxi[391:501,:] # select row from 391 to 500 and all columns
# row_21_column_5 = taxi[21,5] # select element [21,5]

# # From the taxi ndarray:
# # - Select every row for the columns at indexes 1, 4, and 7 and assign them to columns_1_4_7.
# # - Select the columns at indexes 5 to 8 inclusive for the row at index 99 and assign them to row_99_columns_5_to_8.
# # - Select the rows at indexes 100 to 200 inclusive for the column at index 14 and assign them to rows_100_to_200_column_14.
# columns_1_4_7 = taxi[:,[1,4,7]]
# row_99_columns_5_to_8 = taxi[99,5:9]
# rows_100_to_200_column_14 = taxi[100:201,14]

# # - Use vector division to divide trip_distance_miles by trip_length_hours, assigning the result to trip_mph.
# # - After you have run your code, use the variable inspector below the code box to inspect the contents of the new trip_mph variable.
# trip_distance_miles = taxi[:,7]
# trip_length_seconds = taxi[:,8]
# trip_length_hours = trip_length_seconds / 3600 # 3600 seconds is one hour
# trip_mph = trip_distance_miles/trip_length_hours

# # - Use the ndarray.max() method to calculate the maximum value of trip_mph and assign the result to mph_max.
# # - Use the ndarray.mean() method to calculate the average value of trip_mph and assign the result to mph_mean.

# mph_min = trip_mph.min()
# mph_max = trip_mph.max()
# mph_mean = trip_mph.mean()

# # - Using a single method, calculate the mean value for each column of taxi, and assign the result to taxi_column_means.

# taxi_column_means = taxi.mean(axis=0)

# # - Expand the dimensions of trip_mph to be a single column in a 2D ndarray, and assign the result to trip_mph_2d.
# # - Add trip_mph_2d as a new column at the end of taxi, assigning the result back to taxi.
# # - Use the print() function to display taxi and view the new column.

# trip_mph_2d = np.expand_dims(trip_mph,axis=1)
# taxi = np.concatenate([taxi,trip_mph_2d],axis=1)
# print(taxi)

int_square = [[5, 2, 8, 3, 4],
				[2, 8, 6, 2, 5],
				[1, 6, 2, 7, 7],
				[0, 7, 7, 4, 5],
				[5, 7, 1, 1, 2]]

int_square = np.array(int_square)

last_column = int_square[:,4]
print(last_column)

# returns the indices of last_column which will sort the array according to the last column's value
sorted_order = np.argsort(last_column)
print(sorted_order)
# output: [4 0 1 3 2]

# sort the last column only
last_column_sorted = last_column[sorted_order]
print(last_column_sorted)
# output: [2 4 5 5 7]

# sort based on the last column

int_square_sorted = int_square[sorted_order]
# output: [[5 7 1 1 2]
# 		   [5 2 8 3 4]
#          [2 8 6 2 5]
#          [0 7 7 4 5]
#          [1 6 2 7 7]]