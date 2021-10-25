from datetime import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt


#Loading the data from the DATA_PATH

DATA_PATH ="export_trajets.csv"
df = pd.read_csv(DATA_PATH, delimiter = ",",header = 0)

# Here we drop two columns that aren't needed
df_=df.drop(['mode','purpose'],axis=1)

# Then we modify the type of the column "starttime" and "endtime" to have it in a date format
df[['starttime','endtime']]=df.apply(lambda x : x[['starttime','endtime']].astype('datetime64'),axis=1)

# We extract the (day,hour and day name from this date) and make three new columns with those new features

df['day'] = df['starttime'].dt.day
df['hour'] = df['starttime'].dt.hour
df['day_name'] = df['starttime'].dt.day_name()

## Get the demand for weekdays and weekend 
# Create two dataset : one with all trips that are made on weekdays and 
# one with all the trips done during the weekend.

weekdays=df.loc[~((df['day_name']=='Saturday')|(df['day_name']=='Sunday'))]
weekend=df.loc[(df['day_name']=='Saturday')|(df['day_name']=='Sunday')]

## Then we can grouped by day and hour and count how many trip we have for those hours/day [ for weekdays]

group_weekdays=weekdays.groupby(['day_name','hour']).count()['id_trip']
group_weekdays=group_weekdays.unstack()

## Same for Weekend 

group_weekend=weekend.groupby(['day_name','hour']).count()['id_trip']
group_weekend=group_weekend.unstack()

# the following will plot the graph for the congestion for both weekdays and weekend 

# plot aspect

plt.rcParams['figure.figsize'] = [9, 6]
plt.rcParams['figure.dpi'] = 100 # 200 e.g. is really fine, but slower
font = {'family' : 'DejaVu Sans',
        'weight' : 'normal',
        'size'   : 18}

plt.rc('font', **font)

# plot weekday

plt.plot(group_weekdays.T)
plt.xlabel('Hour of the Day ')
plt.ylabel('Number of Trip ')
plt.ylim(0,3500)
plt.legend(group_weekdays.T.columns,bbox_to_anchor=(0.05, 0.95), loc=2, borderaxespad=0.)
plt.savefig('week.jpg')
plt.show()

# plot weekend

plt.plot(group_weekend.T)
plt.xlabel('Hour of the Day ')
plt.ylabel('Number of Trip ')
plt.ylim(0,3500)
plt.legend(group_weekend.T.columns,bbox_to_anchor=(0.05, 0.95), loc=2, borderaxespad=0.)
plt.savefig('weekend.jpg')