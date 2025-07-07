# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 18:05:41 2024

@author: HP
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from termcolor import colored

#Load dataset->

df = pd.read_csv(r'banking_data.csv')


#pd.set_option
#Examining the data->
#Displaying rows w/o truncation setting them to none means there are no max limit and all rows or column will be displayed w/o truncation
pd.set_option('display.max_rows' , None)
pd.set_option('display.max_columns' , None)







print(colored("\n\n\n\n\n\n\n------------------------------------------------------------------------------------------------------------------------\n\n\n\n\n\n\n", "green"))







# 1)Distribution of age among the clients->


print(colored('Answer ->1)Distribution of age among the clients->\n', 'magenta', attrs=['underline' , 'bold']))
print(colored("************************************************************************************" , 'red'))
print("See the 'plot' subpanel to see the distribution of age with clients")
print(colored("************************************************************************************\n" , 'red'))

plt.hist(df['age'] , color = 'green' , edgecolor = 'black')
plt.xlabel("Age")
plt.ylabel('Frequency')
plt.title('Ans -> 1) Distribution of age (in years) among the clients')
plt.xticks(rotation=90)
plt.show()

print("-----------------------------------------------------")

print(colored('Distribution of age with clients->\n', 'yellow', attrs=['underline' , 'bold']))

age_distribution = df['age'].value_counts().reset_index()
age_distribution.columns = ['Age', 'Count']
age_distribution = age_distribution.sort_values(by='Age').reset_index(drop=True)
print(age_distribution)

print("-----------------------------------------------------")

#Calculate total missing age data
missing_age_count = df['age'].isnull().sum()

# Calculate standard deviation
std_dev = df['age'].std()

# Calculate mode
mode_age = df['age'].mode()[0]

# Calculate range
range_age = df['age'].max() - df['age'].min()

# Calculate median
median_age = df['age'].median()

print(colored('\nFor further analysis........(it includes details such as count of observation , mean value , min and max values  , quartile val)->\n', 'yellow', attrs=['underline' , 'bold']))

print("Missing data  ",missing_age_count)
print(f"Standard Deviation   {std_dev}")
print(f"Mode        {mode_age}")
print(f"Range       {range_age}")
print( f"Median      {median_age}")
print(df['age'].describe())

print("-----------------------------------------------------")

if not(missing_age_count) :
    print(colored("\n**Since count is  full, hence no data under age  column is missing.", "cyan"))
else:
  print(colored("\n**Since count is not full, hence some data under age column is missing.", "cyan"))







print(colored("\n\n\n\n\n\n\n------------------------------------------------------------------------------------------------------------------------\n\n\n\n\n\n\n", "green"))






# 2)Distribution of job among the clients->


print(colored('Answer ->2)Distribution of job among the clients->\n', 'magenta', attrs=['underline' , 'bold']))
print(colored("************************************************************************************" , 'red'))
print("See the 'plot' subpanel to see the distribution of job with clients")
print(colored("************************************************************************************\n" , 'red'))

job_counts = df['job'].value_counts()
plt.figure(figsize=(10, 6))
sns.barplot(x=job_counts.index, y=job_counts.values, palette='viridis')
plt.xlabel("Job")
plt.ylabel('Frequency')
plt.title('Ans -> 2) Distribution of job')
plt.xticks(rotation=90)
plt.show()

print("-----------------------------------------------------")

job_distribution = df['job'].value_counts().reset_index()
job_distribution.columns = ['Job', 'Count']

print(colored('Distribution of job with clients->\n', 'yellow', attrs=['underline' , 'bold']))
print(job_distribution)

print("-----------------------------------------------------")

#Calculate total missing job data
missing_job_count = df['job'].isnull().sum()


print(colored('\nFor further analysis........(it includes details such as count of observation , top(most frequent) , freq = frequency of top )....->\n', 'yellow', attrs=['underline' , 'bold']))
print("Missing data  ",missing_job_count)
print(df['job'].describe())

print("-----------------------------------------------------")


if not(missing_job_count) :
    print(colored("\n**Since count is  full, hence no data under job column is missing.", "cyan"))
else:
  print(colored("\n**Since count is not full, hence some data under job column is missing.", "cyan"))








print(colored("\n\n\n\n\n\n\n------------------------------------------------------------------------------------------------------------------------\n\n\n\n\n\n\n", "green"))







# 3)marital status distribution of the clients->


print(colored('Answer ->3)Marital status distribution of the clients->\n', 'magenta', attrs=['underline' , 'bold']))
print(colored("************************************************************************************" , 'red'))
print("See the 'plot' subpanel to see the distribution of marital status among clients")
print(colored("***********************************************************************************\n" , 'red'))

marital_counts = df['marital'].value_counts()
plt.figure(figsize=(7, 6))
sns.barplot(x=marital_counts.index, y=marital_counts.values, palette='PuBuGn')
plt.xlabel("Marital Status")
plt.ylabel('Frequency')
plt.title('Ans -> 3) Distribution of Marital Status')
plt.xticks(rotation=90)
plt.show()

print("-----------------------------------------------------")

# Calculate the distribution of marital statuses 
marital_distribution = df['marital'].value_counts().reset_index()
marital_distribution.columns = ['Marital Status', 'Count']
print(colored('Distribution of marital status with clients->\n', 'yellow', attrs=['underline' , 'bold']))
print(marital_distribution)

print("-----------------------------------------------------")

#Calculate total missing marital status data
missing_marital_count = df['marital'].isnull().sum()


print(colored('\nFor further analysis........(it includes details such as count of observation , top(most frequent) , freq = frequency of top )....->\n', 'yellow', attrs=['underline' , 'bold']))
print("Missing data  ",missing_marital_count)
print(df['marital'].describe())

print("-----------------------------------------------------")

if not(missing_marital_count) :
    print(colored("\n**Since count is full, hence no data under marital status column is missing.", "cyan"))

else:
  print(colored("\n**Since count is not full, hence some data under marital status column is missing.", "cyan"))







print(colored("\n\n\n\n\n\n\n------------------------------------------------------------------------------------------------------------------------\n\n\n\n\n\n\n", "green"))









# 4) Education level distribution of the clients

print(colored('Answer -> 4) Education level distribution of the clients->\n', 'magenta', attrs=['underline', 'bold']))
print(colored("************************************************************************************" , 'red'))
print("See the 'plot' subpanel to see the distribution of education level among clients")
print(colored("************************************************************************************\n" , 'red'))
education_counts = df['education'].value_counts()
plt.figure(figsize=(7, 6))
sns.barplot(x=education_counts.index, y=education_counts.values, palette='viridis')
plt.xlabel("Education Level")
plt.ylabel('Frequency')
plt.title('Ans -> 4) Distribution of Education Level')
plt.xticks(rotation=90)  # Rotate the labels on the x-axis by 90 degrees
plt.show()

print("-----------------------------------------------------")

# Calculate the distribution of education levels
education_distribution = df['education'].value_counts().reset_index()
education_distribution.columns = ['Education Level', 'Count']
print(colored('Distribution of education level with clients->\n', 'yellow', attrs=['underline', 'bold']))
print(education_distribution)

print("-----------------------------------------------------")

# Calculate total missing education data
missing_education_count = df['education'].isnull().sum()

print(colored('\nFor further analysis........(it includes details such as count of observation, top (most frequent), freq = frequency of top)....->\n', 'yellow', attrs=['underline', 'bold']))
print("Missing data: ", missing_education_count)
print(df['education'].describe())

print("-----------------------------------------------------")

if not(missing_education_count) :
    print(colored("\n**Since count is full, hence no data under education column is missing.", "cyan"))

else:
  print(colored("\n**Since count is not full, hence some data under education column is missing.", "cyan"))







print(colored("\n\n\n\n\n\n\n------------------------------------------------------------------------------------------------------------------------\n\n\n\n\n\n\n", "green"))







# 5) Proportion of clients who have credit in default->

print(colored('Answer -> 5) Proportion of clients who have credit in default->\n', 'magenta', attrs=['underline', 'bold']))
missing_default_count = df['default'].isnull().sum()

print(colored("********************************************************************************************************" , 'red'))
print(f"Missing  --->  {missing_default_count}")
if (not missing_default_count) :
    print("Since there is no missing data under default credit section , there's no need to worry about nan(missing) values")
print(colored("********************************************************************************************************\n" , 'red'))

default_counts = df["default"].value_counts()
total_default_yes = default_counts.get('yes', 0)#defaults to 0
print("Total no. of clients who have credit in default ---> ",total_default_yes )

total_entery = df['default'].count()
print("Total enteries from default credit column ---> " , total_entery)

proportion_of_yes = total_default_yes/total_entery
print(f"Proportion of clients who have credit in default  --->  {proportion_of_yes}")







print(colored("\n\n\n\n\n\n\n------------------------------------------------------------------------------------------------------------------------\n\n\n\n\n\n\n", "green"))







# 6) Distribution of average yearly balance among the clients->

print(colored('Answer ->6) Distribution of average yearly balance(in euros) among the clients->\n', 'magenta', attrs=['underline', 'bold']))
print(colored("************************************************************************************", 'red'))
print("See the 'plot' subpanel to see the distribution of average yearly balance among clients")
print(colored("************************************************************************************\n", 'red'))

plt.hist(df['balance'], color='magenta', edgecolor='black')
plt.xlabel("Average Yearly Balance (in euros)")
plt.ylabel('Frequency')
plt.title('Ans -> 6) Distribution of Average Yearly Balance (in euros) among the Clients')
plt.xticks(rotation=90) 
plt.show()

print("-----------------------------------------------------")

print(colored('Distribution of average yearly balance (in euros) among clients->\n(in intervals)', 'yellow', attrs=['underline', 'bold']))

num_bins = 5 
df['balance_bins'] = pd.cut(df['balance'], bins=num_bins)

# Count the occurrences in each bin
balance_distribution = df['balance_bins'].value_counts().reset_index()
balance_distribution.columns = ['Balance Interval(in euros)', 'Count']
balance_distribution = balance_distribution.sort_values(by='Balance Interval(in euros)').reset_index(drop=True)
print(balance_distribution)


print("-----------------------------------------------------")

# Calculate total missing balance data
missing_balance_count = df['balance'].isnull().sum()

# Calculate standard deviation
std_dev_balance = df['balance'].std()

# Calculate mode
mode_balance = df['balance'].mode()[0]

# Calculate range
range_balance = df['balance'].max() - df['balance'].min()

# Calculate median
median_balance = df['balance'].median()

print(colored('\nFor further analysis........(it includes details such as count of observation, mean value, min and max values, quartile values)->\n', 'yellow', attrs=['underline', 'bold']))

print("Missing data ", missing_balance_count)
print(f"Standard Deviation {std_dev_balance}")
print(f"Mode      {mode_balance}")
print(f"Range     {range_balance}")
print(f"Median    {median_balance}")
print(df['balance'].describe())

print("-----------------------------------------------------")

if not(missing_balance_count) :
    print(colored("\n**Since count is full, hence no data under balance column is missing.", "cyan"))

else:
  print(colored("\n**Since count is not full, hence some data under balance column is missing.", "cyan"))









print(colored("\n\n\n\n\n\n\n------------------------------------------------------------------------------------------------------------------------\n\n\n\n\n\n\n", "green"))







# 7)No. of clients having housing loans->

print(colored('Answer -> 7) Total client base who have a housing loan->\n', 'magenta', attrs=['underline', 'bold']))
missing_housing_loan_count = df['housing'].isnull().sum()

housing_loan_counts = df["housing"].value_counts()
total_housing_loan_yes = housing_loan_counts.get('yes', 0)  # Defaults to 0
print("Total no. of client base who have a housing loan ---> ", total_housing_loan_yes)

print("\n-----------------------------------------------------")

print(f"\nMissing  --->  {missing_housing_loan_count}")
if (not missing_housing_loan_count):
    print("Since there is no missing data under housing section, there's no need to worry about nan(missing) values.")






print(colored("\n\n\n\n\n\n\n------------------------------------------------------------------------------------------------------------------------\n\n\n\n\n\n\n", "green"))







# 8)No. of clients having personal loans->

print(colored('Answer -> 8) Total client base who have a personal loan->\n', 'magenta', attrs=['underline', 'bold']))
missing_loan_count = df['loan'].isnull().sum()

loan_counts = df["loan"].value_counts()
total_loan_yes  = loan_counts.get('yes', 0)  # Defaults to 0
print("Total no. of client base who have a personal loan ---> ", total_loan_yes)

print("\n-----------------------------------------------------")

print(f"\nMissing  --->  {missing_loan_count}")
if (not missing_loan_count):
    print("Since there is no missing data under loan section, there's no need to worry about nan(missing) values.")






print(colored("\n\n\n\n\n\n\n------------------------------------------------------------------------------------------------------------------------\n\n\n\n\n\n\n", "green"))







# 9)The communication types used for contacting clients during the campaign

print(colored('Answer -> 9) The communication types used for contacting clients during the campaign->\n', 'magenta', attrs=['underline', 'bold']))
communication_types = df['contact'].unique()


print(colored('Communication types used for contacting clients during the campaign:', 'yellow', attrs=['underline', 'bold']))
for communication_type in communication_types:
    print("- ", communication_type)
    
print("\n-----------------------------------------------------")

print(colored('\nFor further reference you could also see.....-> ', 'yellow', attrs=['underline', 'bold']))    
communication_distribution = df['contact'].value_counts().reset_index()
communication_distribution.columns = ['Communication Type', 'Count']
print(colored('Distribution of communication types used for contacting clients->\n', 'yellow', attrs=['underline', 'bold']))
print(communication_distribution)







print(colored("\n\n\n\n\n\n\n------------------------------------------------------------------------------------------------------------------------\n\n\n\n\n\n\n", "green"))







# 10)Distribution of Last contact day of the month
print(colored('Answer -> 10) Last contact day distribution of the clients->\n', 'magenta', attrs=['underline', 'bold']))
print(colored("************************************************************************************", 'red'))
print("See the 'plot' subpanel to see the distribution of last contact day of the month among clients")
print(colored("***********************************************************************************\n", 'red'))

contact_day_counts = df['day'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
sns.barplot(x=contact_day_counts.index, y=contact_day_counts.values, palette='viridis')
plt.xlabel("Last contact day of the Month")
plt.ylabel('Frequency')
plt.title('Ans -> 10) Distribution of last contact day of the month ')
plt.xticks(rotation=90)
plt.show()

print("-----------------------------------------------------")

# Calculate the distribution of last contact day
contact_day_distribution = df['day'].value_counts().reset_index()
contact_day_distribution.columns = ['Last Contact Day', 'Count']
contact_day_distribution = contact_day_distribution.sort_values(by='Last Contact Day').reset_index(drop=True)
print(colored('Distribution of last contact day with clients->\n', 'yellow', attrs=['underline', 'bold']))
print(contact_day_distribution)

print("-----------------------------------------------------")

missing_contact_day_count = df['day'].isnull().sum()

# Calculate standard deviation
std_dev_day = df['day'].std()

# Calculate mode
mode_day = df['day'].mode()[0]

# Calculate range
range_day = df['day'].max() - df['day'].min()

# Calculate median
median_day = df['day'].median()

print(colored('\nFor further analysis........(it includes details such as count of observation, mean value, min and max values, quartile val)->\n', 'yellow', attrs=['underline', 'bold']))

print("Missing data  ", missing_contact_day_count)
print(f"Standard Deviation   {std_dev_day : .6f}")
print(f"Mode        {mode_day}")
print(f"Range       {range_day}")
print(f"Median      {median_day}")
print(df['day'].describe())

print("-----------------------------------------------------")

if not(missing_contact_day_count) :
    print(colored("\n**Since count is full, hence no data under day column is missing.", "cyan"))

else:
  print(colored("\n**Since count is not full, hence some data under day column is missing.", "cyan"))











print(colored("\n\n\n\n\n\n\n------------------------------------------------------------------------------------------------------------------------\n\n\n\n\n\n\n", "green"))






#11) Distribution of last contact month among the client
print(colored('Answer -> 11)Distribution of last contact month among the clients->\n', 'magenta', attrs=['underline', 'bold']))
print(colored("************************************************************************************", 'red'))
print("See the 'plot' subpanel to see the distribution of last contact month among clients")
print(colored("************************************************************************************\n", 'red'))

month_counts = df['month'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
sns.barplot(x=month_counts.index, y=month_counts.values, palette='PuBuGn')
plt.xlabel("Last Contact Month")
plt.ylabel('Frequency')
plt.title('Ans-> 11) Distribution of Last Contact Month')
plt.xticks(rotation=90)
plt.show()

print("-----------------------------------------------------")

month_distribution = df['month'].value_counts().reset_index()
month_distribution.columns = ['Last Contact Month', 'Count']
month_distribution = month_distribution.sort_values(by='Last Contact Month').reset_index(drop=True)
print(colored('Distribution of last contact month with clients->\n', 'yellow', attrs=['underline', 'bold']))
print(month_distribution)

print("-----------------------------------------------------")

missing_month_count = df['month'].isnull().sum()


print(colored('\nFor further analysis........(it includes details such as count of observation, top (most frequent), freq = frequency of top)->\n', 'yellow', attrs=['underline', 'bold']))
print("Missing data  ", missing_month_count)
print(df['month'].describe())

print("-----------------------------------------------------")

if not(missing_month_count) :
    print(colored("\n**Since count is full, hence no data under 'month' column is missing.", "cyan"))

else:
  print(colored("\n**Since count is not full, hence some data under 'month' column is missing.", "cyan"))







print(colored("\n\n\n\n\n\n\n------------------------------------------------------------------------------------------------------------------------\n\n\n\n\n\n\n", "green"))






#12) Distribution of duration of the last contact among the clients
print(colored('Answer ->12 Distribution of duration of the last contact among the clients->\n', 'magenta', attrs=['underline', 'bold']))
print(colored("*************************************************************************************************", 'red'))
print("See the 'plot' subpanel to see the distribution of the duration of the last contact among clients")
print(colored("*************************************************************************************************\n", 'red'))

plt.hist(df['duration'], color='blue', edgecolor='black')
plt.xlabel("Duration of Last Contact (in seconds)")
plt.ylabel('Frequency')
plt.title('Ans -> 12) Distribution of Duration of Last Contact (in seconds) among the Clients')
plt.xticks(rotation=90)  # Rotate the labels on the x-axis by 90 degrees
plt.show()

print("-----------------------------------------------------")

print(colored('Distribution of duration of the last contact among clients(in intervals)->\n', 'yellow', attrs=['underline', 'bold']))

num_bins = 5  # Dividing into 5 intervals


df['duration_bins'] = pd.cut(df['duration'], bins=num_bins)
duration_distribution = df['duration_bins'].value_counts().reset_index()
duration_distribution.columns = ['Duration Interval (in seconds)', 'Count']
duration_distribution = duration_distribution.sort_values(by='Duration Interval (in seconds)').reset_index(drop=True)
print(duration_distribution)

print("-----------------------------------------------------")

# Calculate total missing duration data
missing_duration_count = df['duration'].isnull().sum()

# Calculate standard deviation
std_dev_duration = df['duration'].std()

# Calculate mode
mode_duration = df['duration'].mode()[0]

# Calculate range
range_duration = df['duration'].max() - df['duration'].min()

# Calculate median
median_duration = df['duration'].median()

print(colored('\nFor further analysis........(it includes details such as count of observation, mean value, min and max values, quartile values)->\n', 'yellow', attrs=['underline', 'bold']))

print("Missing data ", missing_duration_count)
print(f"Standard Deviation {std_dev_duration : .6f}")
print(f"Mode     {mode_duration}")
print(f"Range    {range_duration}")
print(f"Median   {median_duration}")
print(df['duration'].describe())

print("-----------------------------------------------------")

if not(missing_duration_count) :
    print(colored("\n**Since count is full, hence no data under 'duration' column is missing.", "cyan"))

else:
  print(colored("\n**Since count is not full, hence some data under 'duration' column is missing.", "cyan"))

    




print(colored("\n\n\n\n\n\n\n------------------------------------------------------------------------------------------------------------------------\n\n\n\n\n\n\n", "green"))







#13) Display the number of contacts for each client
print(colored('Answer ->13 Number of contacts performed during the campaign for each client->\n', 'magenta', attrs=['underline', 'bold']))
print(colored("************************************************************************************", 'red'))
print("Here are the number of contacts performed during the campaign for each client-->")
print(colored("************************************************************************************\n", 'red'))

print(df[['campaign']])







print(colored("\n\n\n\n\n\n\n------------------------------------------------------------------------------------------------------------------------\n\n\n\n\n\n\n", "green"))







#14) Distribution of the number of days passed since the client was last contacted from a previous campaign->
print(colored('Answer ->14) Distribution of the number of days passed since the client was last contacted from a previous campaign->\n', 'magenta', attrs=['underline', 'bold']))
print(colored("-->-1 means the client was not previously contacted.", 'red', attrs=['bold' , 'underline']))
print(colored("************************************************************************************************************************************************", 'red'))
print("See the 'plot' subpanel to see the distribution of the number of days passed since the client was last contacted from a previous campaign")
print(colored("************************************************************************************************************************************************\n", 'red'))

# Plot the distribution of pdays
plt.figure(figsize=(10, 6))
plt.hist(df['pdays'], bins=30, color='cyan', edgecolor='black')
plt.xlabel("Number of days passed since the client was last contacted")
plt.ylabel('Frequency')
plt.title('Ans -> 14) Distribution of Number of Days Passed Since Last Contact from Previous Campaign')
plt.xticks(rotation=90)
plt.show()

print("-----------------------------------------------------")

num_bins = 10  
df['pdays_bins'] = pd.cut(df['pdays'], bins=num_bins)
pdays_distribution_intervals = df['pdays_bins'].value_counts().reset_index()
pdays_distribution_intervals.columns = ['Number of days passed ', 'Count']
pdays_distribution_intervals = pdays_distribution_intervals.sort_values(by='Number of days passed ').reset_index(drop=True)
print(colored('Distribution of number of days passed since the client was last contacted from a previous campaign (in intervals)->\n', 'yellow', attrs=['underline', 'bold']))
print(pdays_distribution_intervals)

print("-----------------------------------------------------")

# Calculate total missing pdays data
missing_pdays_count = df['pdays'].isnull().sum()

# Calculate standard deviation
std_dev_pdays = df['pdays'].std()

# Calculate mode
mode_pdays = df['pdays'].mode()[0]

# Calculate range
range_pdays = df['pdays'].max() - df['pdays'].min()

# Calculate median
median_pdays = df['pdays'].median()

print(colored('\nFor further analysis........(it includes details such as count of observation, mean value, min and max values, quartile values)->\n', 'yellow', attrs=['underline', 'bold']))

print("Missing data ", missing_pdays_count)
print(f"Standard Deviation {std_dev_pdays}")
print(f"Mode       {mode_pdays}")
print(f"Range      {range_pdays}")
print(f"Median     {median_pdays}")
print(df['pdays'].describe())

print("-----------------------------------------------------")


if not(missing_pdays_count) :
    print(colored("\n**Since count is full, hence no data under 'pdays' column is missing.", "cyan"))

else:
  print(colored("\n**Since count is not full, hence some data under 'pdays' column is missing.", "cyan"))






print(colored("\n\n\n\n\n\n\n------------------------------------------------------------------------------------------------------------------------\n\n\n\n\n\n\n", "green"))







#15) Number of contacts performed before the current campaign for each client->
print(colored('Answer15) -> Number of contacts performed before the current campaign for each client->\n', 'magenta', attrs=['underline', 'bold']))
print(colored("************************************************************************************", 'red'))
print("Here are the number of contacts performed before the current campaign for each client-->")
print(colored("************************************************************************************\n", 'red'))
print(df['previous'])






print(colored("\n\n\n\n\n\n\n------------------------------------------------------------------------------------------------------------------------\n\n\n\n\n\n\n", "green"))








#16) Outcomes of the previous marketing campaigns
print(colored('Answer16) -> Outcomes of the previous marketing campaigns:\n', 'magenta', attrs=['underline', 'bold']))

# Calculate the distribution of the 'poutcome' column
poutcome_counts = df['poutcome'].value_counts()

# Print the distribution of the 'poutcome' column
poutcome_distribution = df['poutcome'].value_counts().reset_index()
poutcome_distribution.columns = ['Outcomes of previous marketing campaigns', 'Count']
poutcome_distribution = poutcome_distribution.sort_values(by='Outcomes of previous marketing campaigns').reset_index(drop=True)
print(colored('Outcomes of previous marketing campaigns->\n', 'yellow', attrs=['underline', 'bold']))
print(poutcome_distribution)

print("-----------------------------------------------------")

print(colored("************************************************************************************************************************************************", 'red'))
print("You could also see the 'plot' subpanel for further inferences to see the outcomes of previous marketing campaigns-->")
print(colored("************************************************************************************************************************************************\n", 'red'))
plt.figure(figsize=(7, 6))
sns.barplot(x=poutcome_counts.index, y=poutcome_counts.values, palette='PuBuGn')
plt.xlabel("Outcome of Previous Marketing Campaign")
plt.ylabel('Frequency')
plt.title('16)Outcomes of Previous Marketing Campaigns')
plt.xticks(rotation=90)
plt.show()

print("-----------------------------------------------------")

# Find the maximum occurring element
mode_poutcome = df['poutcome'].mode()[0]
print("Maximum Occurring Element: ", colored(mode_poutcome, 'cyan'))

# Find the minimum occurring element
min_occurrence = poutcome_counts.idxmin()
print("Minimum Occurring Element: ", colored(min_occurrence, 'cyan'))

print("-----------------------------------------------------")

# Calculate total missing poutcome data
missing_poutcome_count = df['poutcome'].isnull().sum()

print(colored('\nFor further analysis........(it includes details such as count of observation, top (most frequent), freq = frequency of top)->\n', 'yellow', attrs=['underline', 'bold']))

print("Missing data: ", missing_poutcome_count)
print(df['poutcome'].describe())

print("-----------------------------------------------------")

if missing_poutcome_count == 0:
    print(colored("\n**Since count is full, hence no data under 'poutcome' column is missing", "cyan"))
else:
    print(colored("\n**Since count is not full, hence some data under 'poutcome' column is missing", "cyan"))
    






print(colored("\n\n\n\n\n\n\n------------------------------------------------------------------------------------------------------------------------\n\n\n\n\n\n\n", "green"))






# 17) Distribution of clients who subscribed to a term deposit vs. those who did not
print(colored('Answer -> 17) Distribution of clients who subscribed to a term deposit vs. those who did not->\n', 'magenta', attrs=['underline', 'bold']))
print(colored("******************************************************************************************************************", 'red'))
print("See the 'plot' subpanel to see the distribution of clients who subscribed to a term deposit vs. those who did not")
print(colored("******************************************************************************************************************\n", 'red'))

subscription_counts = df['y'].value_counts()
plt.figure(figsize=(7, 6))
sns.barplot(x=subscription_counts.index, y=subscription_counts.values, palette='viridis')
plt.xlabel("Subscription Status")
plt.ylabel('Frequency')
plt.title('Ans -> 17) Distribution of Clients Who Subscribed to a Term Deposit vs. Those Who Did not')
plt.xticks(rotation=90)  # Rotate the labels on the x-axis by 90 degrees
plt.show()

print("-----------------------------------------------------")

# Calculate the distribution of term deposit subscriptions
term_deposit_distribution = df['y'].value_counts().reset_index()
term_deposit_distribution.columns = ['Subscription Status', 'Count']
print(colored('Distribution of clients who subscribed to a term deposit vs. those who did not->\n', 'yellow', attrs=['underline', 'bold']))
print(term_deposit_distribution)

print("-----------------------------------------------------")

mode_poutcome = df['y'].mode()[0]
if mode_poutcome == 'yes':
    print(colored("\nThere are more proportions of clients who subscribed to a term deposit vs. those who did not\n", 'cyan'))
else:
    print(colored("\nThere are more proportions of clients who did not subscribe to a term deposit vs. those who did\n", 'cyan'))

print("-----------------------------------------------------")

# Calculate total missing term deposit subscription data
missing_term_deposit_count = df['y'].isnull().sum()

print(colored('\nFor further analysis........(it includes details such as count of observation, top (most frequent), freq = frequency of top)....->\n', 'yellow', attrs=['underline', 'bold']))
print("Missing data: ", missing_term_deposit_count)
print(df['y'].describe())

print("-----------------------------------------------------")

if missing_term_deposit_count == 0:
    print(colored("\n**Since count is full, hence no data under 'y' column is missing", "cyan"))
else:
    print(colored("\n**Since count is not full, hence some data under 'y' column is missing", "cyan"))
  






print(colored("\n\n\n\n\n\n\n------------------------------------------------------------------------------------------------------------------------\n\n\n\n\n\n\n", "green"))








#18) Correlations between different attributes and the likelihood of subscribing to a term deposit->
print(colored('Answer -> 18) Correlations between different attributes and the likelihood of subscribing to a term deposit->', 'magenta', attrs=['underline', 'bold']))

print("-----------------------------------------------------")

# Explanation of correlation coefficients
explanation = """
Correlation acts like a measuring stick for the intensity relationship between different attributes. 

The correlation coefficient is often denoted as "r"
If r = 1, it indicates a perfect positive linear relationship, meaning that as one variable increases, 
the other variable also increases proportionally.
If r = −1, it indicates a perfect negative linear relationship, meaning that as one variable increases, 
the other variable decreases proportionally.
If r = 0, it indicates no linear relationship between the variables
"""
print(colored(explanation, 'cyan'))

print("Here's something for your reference-->")

# Data for correlation interpretation
data = {
    "Size of correlation(r)": ["0.90 to 1.00 (-0.90 to -1.00)", 
                           "0.70 to 0.90 (-0.70 to -0.90)", 
                           "0.50 to 0.70 (-0.50 to -0.70)", 
                           "0.30 to 0.50 (-0.30 to -0.50)", 
                           "0 to 0.30 (0 to -0.30)"], 
    "Interpretation": ["Very high positive(negative) correlation", 
                       "High positive(negative) correlation", 
                       "Moderate positive(negative) correlation", 
                       "Low positive(negative) correlation", 
                       "Negligible correlation"]
}

# Create DataFrame
df1 = pd.DataFrame(data, index=['a', 'b', 'c', 'd', 'e'])
print(df1)

print("-----------------------------------------------------")

print(colored("*********************************************************************************************************************************", 'red'))
print("See the 'plot' subpanel to see the Correlations between different attributes and the likelihood of subscribing to a term deposit")
print(colored("*********************************************************************************************************************************\n", 'red'))

df['y'] = df['y'].map({'no': -1, 'yes': 1})
df['marital'] = df['marital'].map({'married': 1, 'single': -1, 'divorced': 0})
df['education'] = df['education'].map({'unknown': 0, 'primary': 1, 'secondary': 2, 'tertiary': 3})
df['default'] = df['default'].map({'no': -1, 'yes': 1})
df['housing'] = df['housing'].map({'no': -1, 'yes': 1})
df['loan'] = df['loan'].map({'no': -1, 'yes': 1})
df['contact'] = df['contact'].map({'unknown': 0, 'telephone': 1, 'cellular': 2})
df['poutcome'] = df['poutcome'].map({'unknown': 0, 'other': 1, 'failure': 2, 'success': 3})
df = df.sort_values(by='y')



numeric_df = df.select_dtypes(include = ['int64' , 'float64'])#select column based on data type , here we have selected int , float
corr_matrix = numeric_df.corr()
plt.figure(figsize = (10 , 8))#fig 10 inches in width , 8 inches in ht
sns.heatmap(corr_matrix , annot = True , cmap='PuBuGn' , fmt = ".2f")#corr_matrix  stands for correlation matrix ,  annot = True adds a numerical parameter to each cell in the heat map displaying correlation coefficient value , blue-purple ->low correlation , green-> high correlation , .2f floating pnt no. upto 2 decimal pnt
plt.title('Ans 18) Correlation matrix of banking dataset')
plt.show()



