#-----human resources retention------------------
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle
import numpy as np
import seaborn as sns

df = pd.read_csv('hr_data.csv')

print(df['department'].unique())
print(df['salary'].unique())

eval=pd.read_excel('employee_satisfaction_evaluation.xlsx')

#main=df.set_index('employee_id').join(eval.set_index('EMPLOYEE #')
main=df.join(eval)
main.reset_index()  
main1=main.drop(columns='EMPLOYEE #')  
print(main1.isnull().sum()) 

main1.fillna(main1.mean(),inplace=True)  
#main[main.employee_id==3794]
#main=main.drop(columns='employee_id')         
print(main1.head())

main1.groupby('department').sum()

main1.groupby('department').mean()
#print(main1['left'].value_counts())

def plot_corr(df,size=10):
    corr=df.corr()
    fig,ax=plt.subplots(figsize=(size,size))
    ax.legend()
    cax=ax.matshow(corr)
    fig.colorbar(cax)
    plt.xticks(range(len(corr.columns)),corr.columns,rotation='vertical')
    plt.yticks(range(len(corr.columns)),corr.columns)
    plt.savefig('hr_plotcorr.png')
    plt.show()
#--------------------------------------
plot_corr(main1)
main1=main1.drop(columns='employee_id')
#main1=main1[main1['time_spend_company']>3]
#main1=main1.drop(columns='time_spend_company')
leftdf=main1['left'].value_counts()

plt.figure(figsize=(10,7))
sns.barplot(leftdf.index, leftdf.values, alpha=0.8)
plt.title('Distribution of records for leaving')
plt.ylabel('Number of Occurrences', fontsize=12)
#plt.xlabel('4 clusters', fontsize=12)
plt.savefig('hr_plot_old.png')



plt.figure(figsize=(10,6))
sns.countplot(x = 'average_montly_hours', hue = 'left', data = df, palette = 'magma')
plt.title('Leaving-average_montly_hours')
plt.savefig('hr_monthlyhours.png')
plt.show()
plt.figure(figsize=(10,6))
sns.countplot(x = 'salary', hue = 'left', data = df, palette = 'magma')
plt.title('Leaving-salary')
plt.savefig('hr_Salary_old.png')
plt.show()
plt.figure(figsize=(10,6))
sns.countplot(x = 'department', hue = 'left', data = df, palette = 'OrRd')
plt.title('Leaving-department')
plt.savefig('hr_department_old.png')
plt.show()
plt.figure(figsize=(10,6))
sns.countplot(x = 'time_spend_company', hue = 'left', data = df, palette = 'Blues')
plt.title('Leaving-Time in Company')
plt.savefig('hr_timeincompany_old.png')
plt.show()

plt.figure(figsize=(10,6))
sns.countplot(x = 'Work_accident', hue = 'left', data = df, palette = 'Purples')
plt.title('Leaving-Accidents')
plt.savefig('hr_accident_old.png')
plt.show()
sns.pairplot(main1,hue='left',palette='Dark2')
plt.savefig('hr_paiplot.png')
plt.show()

plt.figure(figsize=(10,7))
sns.set(style='whitegrid')
g=sns.catplot(x='average_montly_hours',y='satisfaction_level',hue='left',data=main1,height=6,kind='bar',palette='muted')
g.despine(left=True)
g.set_ylabels('satisfaction_level')
g.set_xlabels('average_montly_hours')
plt.savefig('hr_catplot_old.png')
plt.show()

plt.figure(figsize=(10,7))
sns.set(style='whitegrid')
g=sns.catplot(x='promotion_last_5years',y='salary',hue='left',data=main1,height=6,kind='bar',palette='muted')
g.despine(left=True)
g.set_ylabels('salary')
g.set_xlabels('promotion')
plt.savefig('hr_catplot_old.png')
plt.show()
#plt.figure(figsize=(10,6))
#sns.jointplot(x='satisfaction_level',y='time_spend_company',data=main1)
#plt.title('leaving')
#plt.ylabel('time_spend_company', fontsize=12)
#plt.xlabel('satisfaction', fontsize=12)
#plt.savefig('hr_joint_old.png')
#plt.show()



plt.figure(figsize=(10,6))
main1.plot.scatter(x='average_montly_hours',y='left')
plt.title('average_montly_hours-left')
plt.ylabel('left', fontsize=12)
plt.xlabel('average_montly_hours', fontsize=12)
plt.savefig('hr_scatter_old.png')
plt.show()
plt.figure(figsize=(10,6))
main1.plot.scatter(x='last_evaluation',y='left')
plt.title('last_evaluation-left')
plt.ylabel('left', fontsize=12)
plt.xlabel('last_evaluation', fontsize=12)
plt.savefig('hr_scatter_evalold.png')
plt.show()


#categorial=['department','salary']
#main1=pd.get_dummies(main1,columns=categorial,drop_first=True)
main1['salary'].replace(('low','medium','high'),(0,1,2),inplace=True)

main1['department'].replace(('sales','accounting','hr','technical','support','management','IT','product_mng','marketing','RandD'),(0,1,2,3,4,5,6,7,8,9),inplace=True)
main2=main1.drop(columns='left')
x=main2.values

y=main1['left'].values

X_train, X_test, y_train, y_test = train_test_split(x, y,
                                                    test_size=0.3,
                                                    random_state=0)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

df_train=pd.DataFrame(X_train)
print(df_train.head())
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

#model=LogisticRegression(solver='lbfgs')
model=RandomForestClassifier()
model.fit(X_train,y_train)
pred=model.predict(X_test)

print("Accuracy {0:.2f}%".format(100*accuracy_score(pred,y_test)))
print(confusion_matrix(y_test,pred))
print(classification_report(y_test,pred))
pickle.dump(model, open('hrmodel.sav', 'wb'))

plt.figure(figsize=(10,6))

plt.bar(range(len(model.feature_importances_)), model.feature_importances_)

plt.xticks(np.arange(9),list(main2.columns[0:]),rotation=20,rotation_mode='anchor',ha='right')
plt.title("Feature's importance")
plt.savefig('hr_featuresold.png')
plt.figure(figsize=(10,6))
sns.lmplot(x='satisfaction_level',y='last_evaluation',data=main1,fit_reg=False,hue='left')

plt.title("Satisfaction-Evaluation")
plt.savefig('hr_lmplot_old.png')
plt.show()

plt.figure(figsize=(10,6))
sns.lmplot(x='satisfaction_level',y='average_montly_hours',data=main1,fit_reg=False,hue='left')

plt.title("Satisfaction-average_montly_hours")
plt.savefig('hr_lmplot_old2.png')
plt.show()
plt.figure(figsize=(10,6))
sns.lmplot(x='satisfaction_level',y='number_project',data=main1,fit_reg=False,hue='left')

plt.title("Satisfaction-number_project")
plt.savefig('hr_lmplot3_old.png')
plt.show()
















