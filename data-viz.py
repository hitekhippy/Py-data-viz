# Requried modules
import pandas as pd
import matplotlib.pyplot as plt

# Read the inpust csv ;
read_csv = pd.read_csv(
    './SEMO-general-technology-group_Member_List_on_04-10-18.csv')

# Grab the unique values in the Joined Group on Column ;
column = read_csv['Joined Group on'].unique().tolist()


# Count the number of joins on each unique date ;
numberOfJoins = read_csv['Joined Group on'].value_counts()

# Plot the bar graph 

plt.bar(column, numberOfJoins, align='center', alpha=0.5)

plt.show()