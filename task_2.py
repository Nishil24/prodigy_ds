import matplotlib.pyplot as plt
import pandas as pd

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
train.head()
# Display basic information about the dataset
print(test.info())

# Display summary statistics
print(test.describe())

# Check for missing values
print(test.isnull().sum())

print(train.isnull().sum())
print(test.describe())

male_ind=len(train[train['Sex'] =='male'])
print("No of Males in Titanic:",male_ind)

female_ind=len(train[train['Sex'] =='female'])
print("No of Females in Titanic:",female_ind)

#plotting
fig=plt.figure()
ax= fig.add_axes([0,0,1,1])
gender=['Male','Female']
index = [157,314]
ax.bar(gender,index)
plt.xlabel("Gender")
plt.ylabel("No of people onboarding ship")
plt.title('Titanic Report')
plt.show()