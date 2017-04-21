

############# Data Cleaning ################

# i am using DOB Job Application Filings dataset from NYC Open Data website
# Data Set url: https://data.cityofnewyork.us/Housing-Development/DOB-Job-Application-Filings/ic3t-wcy2

#import the pandas libary for data load
import pandas as pd
import matplotlib.pyplot as plt


## file path
## https://data.cityofnewyork.us/Education/SAT-College-Board-2010-School-Level-Results/zt9s-n5aj
##file_source = "D:/dyp/data camp/Data Cleaning Project/SAT__College_Board__2010_School_Level_Results.csv"
file_source = "D:/dyp/data camp/Data Cleaning Project/DOB_Job_Application_Filings.csv"

## load csv file using pandas
dt_JobApplication = pd.read_csv(file_source)

## see head rows
dt_JobApplication.head()

## see tail rows
dt_JobApplication.tail()

## check column definations
## through inspection we found Column names has # so 
## we need to clean that
dt_JobApplication.columns

## check the shape of data frame
## we can find rows and column number
dt_JobApplication.shape

## check the data frame info
## to check if NA exist or not
## we can find thea there are number of column having 
## missing data like Community - Board, Landmarked, etc 
## and also Inital Cost, Total Est. Fee are object type due to $ at front

dt_JobApplication.info()

# check the number of applicant in state
# used for categorical data or non-numerical data
dt_JobApplication['State'].value_counts(dropna=False)

#check count for first 5 state
# no missing value so no need to replace
dt_JobApplication['State'].value_counts(dropna=False).head()


## check see if there is null value exist or not in Job Status
## so we need to replace the null value
dt_JobApplication['Job Status'].value_counts(dropna=False)

## to see numerical statistics
## it will give only for numberical data type
dt_JobApplication.describe()

## let see details for specific column Job
dt_JobApplication.describe()['Existing Height']

## let visualized the numerical or continues data 
## through histrogram
dt_JobApplication.info()

dt_JobApplication['Enlargement SQ Footage'].plot('hist')
plt.show()

## lets slice our data and pick existing Height less than 10
## and see the Enlargement SQ Footage
dt_JobApplication[dt_JobApplication['Existing Height']<10]['Enlargement SQ Footage'].plot('hist')





