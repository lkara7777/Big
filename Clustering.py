import pandas as pd
import pickle
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
import seaborn as sns
import pyodbc
#-----------------------------------------------------------------------------------------------------------
#cols=['Product Brand Name','Product Brand Nam','Product Family','Product Name','Country','Age','Sex']
#df = pd.read_csv('pr1.csv',header=None)
#print(df.columns)#30-,40-50
#------connect to database--------------------------------------


def connectToDDS():
    if 'connDDS' not in globals():
        global connDDS 
        connDDS  = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-O3VIQC2\SQLEXPRESS;'
                          'Database=lkdataengineer;'
                          'Trusted_Connection=yes;')
        
       

        
       
    return connDDS
query= """
select * from dbo.clustering
"""
df = pd.read_sql(query, connectToDDS())

df.rename(columns={
                   0:'CandidateId',
                   1:'Brand',
                          2:'Tests',
                          3:'Agegroup',
                          4:'Country',
                          5:'Type',
                          6:'Gender',
                          7:'Promo',
                          8:'Trainer'}, 
                 inplace=True)
#df1=df[(df['Product Family']=="ITIL 4") | (df['Product Family']=="ITIL") | (df['Product Family']=="PPM") | (df['Product Family']=="LSS") | (df['Product Family']=="COBIT5") | (df['Product Family']=="DEVOPS")]

print(df.shape)
df2=df[df['Gender']!="Other"]
df2=df2[df2['Gender']!="Unknown"]
df2.drop(columns=['CandidateId'],inplace=True)
#df2.drop(columns=['Trainer'],inplace=True)
#------------------plotting-----------------------------------------------------

#plt.figure(figsize=(10, 6))
#sns.boxplot(x="Brand", y="NoTests", hue='Gender',data=df2)
#plt.ylabel("Salary in US Dollars", size=14)
#plt.xlabel("Product",size=14)
#plt.title("Brand-NoTests", size=18)
#plt.savefig("boxplot.png")

upsel=df2['Brand'].value_counts()
plt.figure(figsize=(10,7))
sns.barplot(upsel.index, upsel.values, alpha=0.8)
plt.title('Distribution of records for Clustering')
plt.ylabel('Number of Occurrences', fontsize=12)
plt.xlabel('Product', fontsize=12)
plt.savefig('plotmain.png')

plt.figure(figsize=(10,6))
sns.countplot(x = 'Type', hue = 'Brand', data = df, palette = 'magma')
plt.title('Clustering')
plt.savefig('CustomerType.png')
plt.show()
plt.figure(figsize=(10,6))
sns.countplot(x = 'Trainer', hue = 'Brand', data = df, palette = 'Blues')
plt.title('Clustering')
plt.savefig('Trainer.png')
plt.show()
plt.figure(figsize=(10,6))
sns.countplot(x = 'Promo', hue = 'Brand', data = df, palette = 'OrRd')
plt.title('Clustering')
plt.savefig('Promo.png')
plt.show()
plt.figure(figsize=(10,6))
sns.countplot(x = 'Gender', hue = 'Brand', data = df, palette = 'magma')
plt.title('Clustering')
plt.savefig('Gender.png')
plt.show()
print('--------------------')


df2['Gender'].replace(('Male','Female'),(0,1),inplace=True)
df2['Type'].replace(('B2C','B2B'),(0,1),inplace=True)
df2['Trainer'].replace(('No','Yes'),(0,1),inplace=True)
df2['Promo'].replace(('No','Yes'),(0,1),inplace=True)
print(df2['Gender'].value_counts())
print(df2['Brand'].value_counts())

plt.figure(figsize=(10,6))
df2['Country'].value_counts().sort_values(ascending=False).head(10).plot()
plt.title('Countries')
plt.ylabel('Count', fontsize=12)
plt.xlabel('Countries', fontsize=12)
plt.savefig('Countries.png')
plt.show()

df2['Country'].replace(('Afghanistan','Aland Islands','Albania','Algeria','American Samoa','Andorra','Angola','Anguilla','Antarctica','Antigua and Barbuda','Argentina','Armenia','Aruba','Australia',
   'Austria','Azerbaijan','Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Belize','Benin','Bermuda','Bhutan','Bolivia','Bosnia and Herzegovina','Botswana','Bouvet Island','Brazil',
   'British Indian Ocean Territory','Brunei Darussalam','Bulgaria','Burkina Faso','Burundi','Cambodia','Cambodia','Cameroon','Canada','Cape Verde','Caribbean Netherlands','Cayman Islands','Central African Republic',
   'Chad','Chile','China','Christmas Island','Colombia','Comoros','Congo',"Congo, Democratic Republic of the",'Cook Islands','Costa Rica',"CoTE D'IVOIRE",'Croatia','Cuba','CURAcAO','Cyprus','Czech Republic','Denmark',
   'Djibouti','Dominica','Dominican Republic','Ecuador','Egypt','El Salvador','Equatorial Guinea','Eritrea','Estonia','Ethiopia','F.Y.R.O.M.','Falkland Islands (Malvinas)','Faroe Islands','Fiji','Finland','France',
   'French Guiana','French Polynesia','French Southern Territories','Gabon','Gambia','Georgia','Germany','Ghana','Gibraltar','Grenada','Cocos (Keeling) Islands','Greece','Greenland','Guadeloupe','Guam','Guatemala','Guernsey','Guinea','Guinea-Bissau',
   'Guyana','Haiti','Heard Island and McDonald Islands','Honduras','Hong Kong','Hungary','Iceland','India','Indonesia','Iran, Islamic Republic of','Iraq','Ireland','Isle of Man','Israel','Italy','Jamaica',
   'Japan','Jersey','Jordan','Kazakhstan','Kenya','Kiribati',"Korea, Republic of",'Kosovo','Kuwait','Kyrgyzstan',"Lao People΄s Democratic Republic",'Latvia','Lebanon','Lesotho','Liberia','Libyan Arab Jamahiriya','Liechtenstein',
   'Lithuania','Luxembourg','Macao','Madagascar','Malawi','Malaysia','Maldives','Mali','Malta','Marshall Islands','Martinique','Mauritania','Mauritius','Mayotte','Mexico','Micronesia, Federated States of',
   "Moldova, Republic of",'Monaco','Mongolia','Montenegro','Morocco','Mozambique','Myanmar','Namibia','Nepal','Netherlands','New Caledonia','New Zealand','Nicaragua','Niger','Nigeria','Niue','Nauru','Norfolk Island',
   'Northern Mariana Islands','Norway','Oman','Pakistan','Palau',"Palestine, State of",'Panama','Papua New Guinea','Paraguay','Peru','Philippines','Pitcairn','Poland','Portugal','Puerto Rico','Qatar','Reunion','Romania',
   'Russian Federation','Rwanda','Saint Barthélemy','Saint Helena','Saint Kitts and Nevis','Saint Lucia','Saint Martin','Saint Pierre and Miquelon','Saint Vincent and the Grenadines','Samoa',
   'San Marino','Sao Tome and Principe','Saudi Arabia','Senegal','Serbia','Seychelles','Sierra Leone','Singapore','Slovakia','Slovenia','Solomon Islands','Somalia','South Africa','South Georgia and the South Sandwich Islands',
'Spain','Sri Lanka','Sudan','Suriname','Swaziland','Sweden','Switzerland','Syrian Arab Republic','Taiwan, Province of China','Tajikistan',"Tanzania, United Republic of",'Thailand','Timor-Leste','Tokelau','Togo','Tonga',
'Trinidad and Tobago','Tunisia','Turkey','Turkmenistan','Turks and Caicos Islands','Uganda','Ukraine','United Arab Emirates','United Kingdom','United States Minor Outlying Islands','Uruguay','USA','Uzbekistan','Vanuatu',
'Venezuela','Viet Nam',"Virgin Islands, British","Virgin Islands, U.S.",'Western Sahara','Yemen','Zambia','Zimbabwe'),(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,
  34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,
100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,
151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,
203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242),inplace=True)
df2['Brand'].replace(('ITIL','LANGUAGES','OTHER','PPM'),(0,1,2,3),inplace=True)

print(df2['Agegroup'].isnull().sum())
df2=df2.dropna(subset=['Country'])
df2=df2.dropna(subset=['Brand'])
df2=df2.dropna(subset=['Gender'])
df2=df2.dropna(subset=['Trainer'])
df2=df2.dropna(subset=['Promo'])
df2=df2.dropna(subset=['Tests'])
df2=df2.dropna(subset=['Type'])
df2=df2.dropna(subset=['Agegroup'])
df2=df2.dropna(subset=['Agegroup'])

plt.figure(figsize=(10,6))
sns.countplot(x = 'Agegroup', hue = 'Brand', data = df, palette = 'Purples')
plt.title('Clustering')
plt.ylabel('Number of Occurrences', fontsize=12)
plt.xlabel('Age Groups', fontsize=12)
plt.savefig('AgeGroup.png')
plt.show()

df2['Agegroup'].replace(('30-','30-40','40-50','50+'),(0,1,2,3),inplace=True)
#categorical=['Country']
#df2=pd.get_dummies(df2,columns=categorical,drop_first=True)

print(df2.shape)
y=df2.iloc[:,0].values
# Splitting the dataset into the Training set and Test set (20% of our data)
x=df2.iloc[:,1:].values

#-----plotting-------------
#--------------------------------------------------------
sns.pairplot(df2,hue='Brand',palette='Dark2')
plt.savefig('paiplot.png')
plt.show()



#----------------------------------

print(pd.Series(y).value_counts())
# Splitting the dataset into the Training set and Test set (20% of our data)

#from sklearn.externals import joblib 
#import sklearn.metrics as mt
#def Fitmodel(X_train,y_train,X_test,y_test,name,algorithm,gridSearchParams,cv):
#    np.random.seed(10)
#    grid=GridSearchCV(estimator=algorithm,param_grid=gridSearchParams,cv=cv,scoring='accuracy',verbose=1,n_jobs=-1)
#    res=grid.fit(X_train,y_train)
#    best=res.best_params_
 #   pred=res.predict(X_test)
#    print(best)
#    print(mt.classification_report(y_test,pred))
    
    
##from xgboost import XGBClassifier
##param={'n_estimators':[50,100,150,200],'max_depth':[2,4,6]}
#Fitmodel(X_train,y_train,X_test,y_test,'XGBoost',XGBClassifier(n_jobs=-1,objective='softprob'),param,cv=5)



#---------------------------end-------------------------------------------
sc = StandardScaler()
x = sc.fit_transform(x)
from imblearn.over_sampling import SMOTE
se=SMOTE(random_state=42)
x,y=se.fit_resample(x,y)
print(pd.Series(y).value_counts())
# Splitting the dataset into the Training set and Test set (20% of our data)
X_train, X_test, y_train, y_test = train_test_split(x, y,
                                                    test_size=0.22,
                                                    random_state=0)
# Feature Scaling
#sc = StandardScaler()
#X_train = sc.fit_transform(X_train)
#X_test = sc.transform(X_test)

from sklearn.externals import joblib 
#model = RandomForestClassifier(n_estimators = 20, criterion = 'gini', random_state = 42)
model = RandomForestClassifier(random_state = 1234,
                                n_estimators = 100,criterion = 'entropy',
                               max_depth = 22, 
                               min_samples_split = 7,  min_samples_leaf = 1) 
#model=SVC(kernel = 'linear', C = 1)

#from sklearn.neighbors import KNeighborsClassifier 
#model = KNeighborsClassifier(n_neighbors = 7)

model.fit(X_train,y_train)
prediction=model.predict(X_test)
sc1=model.score(X_test,y_test)
print(sc1)
#joblib.dump(model, 'randomforestmodel.sav')
#pickle.dump(model, open('randomforestmodel.sav', 'wb'))
joblib.dump(model, "randomforestmodel.sav")

#predict new row
df3 = pd.read_csv('IT3.csv',header=None)
x=df3.iloc[:,0:].values
print(x)
t = sc.transform(x)
print(t)
pr=model.predict(t)
print(pr)
#classif.report
import sklearn.metrics as mt
report=mt.classification_report(y_test,prediction)
print('\nClassification Report:\n')
print(report)
plt.figure(figsize=(10,6))

plt.bar(range(len(model.feature_importances_)), model.feature_importances_)

plt.xticks(np.arange(9),list(df2.columns[1:]),rotation=90,rotation_mode='anchor',va='top')
plt.title("Feature's importance")
plt.savefig('features0.png')





