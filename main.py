import numpy as np
import pandas as pd

#1
#create a numpy.ndarray (7,7) .print result  in console
matrix = np.zeros((7, 7))
np.fill_diagonal(matrix, 33)
matrix[3, 3] = 77

for i in range(7):
    matrix[i, 0] = 7
    matrix[0, i] = 7
    matrix[i, 6] = 7
    matrix[6, i] = 7
    matrix[0, 0] = 33
    matrix[6, 6] = 33

print(matrix)
#2
#initialize the numpy.ndarray array
nan1=np.full((7,7),np.nan)
matrix1=np.full((7,7),5.0)
matrix1[1:-1,1:-1]=0.0
print(matrix1)
print("\n")

#3 from matrix ex 2 obtain a sub-matrix containing the cells with val = 0
submatrix= matrix1[1:6, 1:6]
print("Submatricea cu valorile 0:\n", submatrix)
#4
#generate a vector of 100 random floating-point values in the range [0,10). create a pandas.Series based on this vector and label its rows as 'L_1','L_2'. print to the console
vector=np.random.uniform(0,10,100)
label=['L_'+str(i+1) for i in range(100) ]
series=pd.Series(vector,index=label)
print(series)
print("\n")

#5
# create a 2-dimensional numpy.ndarray(11,5) of random floating-point values in [0,10). obtain a pandas.DateFrame from this array with row labels of the form 'L1','L2' and column lables of 'C1','C2'. print DateFrame to the console
vector2=np.random.uniform(0,10,(11,5))
rowL=['L'+str(i+1) for i in range(11)]
colL=['C'+str(j+1)for j in range(5)]
df=pd.DataFrame(vector2,index=rowL,columns=colL)
print(df)
print("\n")

#6
#create a dictionary of students with keys of the form 'S_1','S_2'..'S_8'. the dictionary values are lists of 7 random grades from 1 to 10. create a pandas.DataFrame from the dictionary and print to the cons.
dict1={'S_'+str(j+1):[j for j in np.random.randint(1,10+1,7).tolist()]for j in range(8)}
df2=pd.DataFrame(dict1)
print(df2)
print("\n")

#7
#create a pandas.DataFrame from a python dictionary whose keys are students of the form 'Stud1'...'stud7' and whose values are pandas. series of 5 random grades from 1 to 10, labelled 'EX1'..'Ex5'. prinT DF to the cons
dict2={'Stud'+str(k+1):pd.Series(np.random.randint(1,10+1,5), index=['Ex'+str(k1+1) for k1 in range(1,6)])for k in range(8)}
df7=pd.DataFrame(dict2)
print(df7)
print("\n")


#8
#read tbe files Series1_csv adn Series2_csv and bring the date into 2 pandas.Series. create a python dictionary with the keys 'Col1','Col2' and having as values the 2 Series with the data taken from the files. create a pandas.DF from the previuosly created dictionary and print it to console.
series1 = pd.read_csv('./dataIN/Series_1.csv', index_col=0).iloc[:, 0]
series2 = pd.read_csv('./dataIN/Series_2.csv', index_col=0).iloc[:, 0]

print("Series 1:")
print(series1)
print("\nSeries 2:")
print(series2)

series1, series2 = series1.align(series2, join='outer')
merged_dict = {"Col1": series1, "Col2": series2}
merged_df = pd.DataFrame(merged_dict)
print(merged_df)
print("\n")


#9
#create a dictionary where the keys are years of study of the form 'An1',..'An5' and the values are dictionaries with keys of the form 'Stud1'...'Stud8' anf the values are 5 random grades from 1 to 10. create a pandas.DF from this dictionary of dictionaries and print it to cons.
dict4 = {
    'An' + str(i + 1): {
        'Stud' + str(j + 1): np.random.randint(1, 11, 5).tolist()
        for j in range(8)
    }
    for i in range(5)
}
df_list = []
for year, students in dict4.items():
    year_df = pd.DataFrame(students)
    year_df.index = ['Ex' +str(k+1) for k in range(5)]
    year_df['An'] = year
    df_list.append(year_df)

final_df = pd.concat(df_list)

print(final_df)
