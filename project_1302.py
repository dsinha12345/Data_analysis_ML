import pandas as pd 
import pandas.read_csv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor
'''
Abstract: Accelerometer data from vibrations of a cooler fan with weights on its blades. It can be used for predictions, classification and other tasks that require vibration analysis, especially in engines.

Data Set Information:

This dataset was generated for use on 'Prediction of Motor Failure Time Using An Artificial Neural Network' project (DOI: 10.3390/s19194342). A cooler fan with weights on its blades was used to generate vibrations. To this fan cooler was attached an accelerometer to collect the vibration data. With this data, motor failure time predictions were made, using an artificial neural networks. To generate three distinct vibration scenarios, the weights were distributed in three different ways: 1) 'red' - normal configuration: two weight pieces positioned on neighboring blades; 2) 'blue' - perpendicular configuration: two weight pieces positioned on blades forming a 90Â° angle; 3) 'green' - opposite configuration: two weight pieces positioned on opposite blades. A schematic diagram can be seen in figure 3 of the paper.

Devices used:
Akasa AK-FN059 12cm Viper cooling fan (Generate the vibrations)
MMA8452Q accelerometer (Measure vibration)

Data collection method:
17 rotation speeds were set up, ranging from 20% to 100% of the cooler maximum speed at 5% intervals; for the three weight distribution configurations in the cooler blades. Note that the Akasa AK-FN059 cooler has 1900 rpm of max rotation speed.

The vibration measurements were collected at a frequency of 20 ms for 1 min for each percentage, generating 3000 records per speed. Thus, in total, 153,000 vibration records were collected from the simulation model.


Attribute Information:

There are 5 attributes in the dataset: wconfid,pctid,x,y and z.

wconfid: Weight Configuration ID (1 - 'red' - normal configuration; 2 - 'blue' - perpendicular configuration; 3 - 'green' - opposite configuration)
pctid: Cooler Fan RPM Speed Percentage ID (20 means 20%, and so on).
x: Accelerometer x value.
y: Accelerometer y value.
z: Accelerometer z value.
'''

def manipulation(df):    
    print(''' 
    1. Insert a rows\n
    2. Delete a rows\n''')
    mch=int(input("Enter your choice")) 
    if mch==1:
         col=df.columns
         print(col)
         print(df.head(1))
         j=0
         ninsert={}
         for i in col:
             print("Enter ", col[j], " value")
             nval=input()
             ninsert[col[j]]=nval
             j=j+1
             print(ninsert)
             df = df.append(ninsert, ignore_index=True)
             print("New row inserted")
    elif mch == 2:
        dropindex = int(input("ENTER THE INDEX OF ROW YOU WANT TO DELETE: "))
        df.drop(df.index[dropindex], inplace = True)
        print(df)

def analysis(df):
    print("Data Frame Analysis")
    menu=''' 1. Top record
 \n 2. Bottom Records
 \n 3. To display complete statitics of the dataframe
 \n 4. To display complete information about dataframe
 \n 5. to exit the program
 '''
    print(menu)
    while True:
        try:
            ch3=int(input("Enter your choice: "))
            if ch3==1:
                n=int(input("Enter the number of records to be displayed: "))
                print("Top ", n," records from the dataframe")
                print(df.head(n))
            elif ch3==2:
                n=int(input("Enter the number of records to be displayed: "))
                print("Bottom ", n," records from the dataframe")
                print(df.tail(n))
            elif ch3==3:
                print("Complete Statistics")
                stat_df=df.iloc[:,2 : :]
                print(stat_df.agg(['min', 'max',"var","std","mean","median"]))
                print("We can the statistics of the vibrations in all the direction of a cartesian plane")
            elif ch3==4:
                print("Information about dataframe")
                print(df.info())
            elif ch3 ==5:
                break
        except ValueError:
            print("enter the value correctly")
            continue
def Visualisation(df):
    print("Data Visualisation of pandas data frame")
    menu=''' 1. To display histogram of all numeric columns
 \n 2. To display the line chart
 \n 3. To display scatter plot between pctid and acceleration
 \n 4. To see every kind of scatter plot 
 \n 5. To exit
 '''
    print(menu)
    while True:
        try:
            ch4=int(input("Enter your choice"))
            if ch4==1:
                fig, axs = plt.subplots(2, 2)
                axs[0, 0].hist(df.x)
                axs[0, 0].set_title('x')
                axs[0, 1].hist(df.y)
                axs[0, 1].set_title('y')
                axs[1, 0].hist(df.x)
                axs[1, 0].set_title('z')
                axs[1, 1].hist(df.acceleration)
                axs[1, 1].set_title('acc')
                plt.show()
            elif ch4==2:
                df[["x","y","z","acceleration"]].plot()
                plt.xlabel("indexes")
                plt.legend()
                plt.show()
            elif ch4==3:
                plt.scatter(df.pctid, df.acceleration, c=df.wconfid)
                plt.xlabel("Cooler fan speed percentage")
                plt.ylabel("acceleration")
                plt.legend(df.wconfid,title="wconfid")
                plt.title("Scatter plot between acceleration and Cooler fan spped percentage")
                plt.show()
            elif ch4==4:
                sns.pairplot(df,diag_kind='kde') 
                plt.show()
            elif ch4==5:
                break
        except ValueError:
            print("enter correct value")
            continue

def test_train_data(df):
     

     x=df[["wconfid","pctid"]]
     y=df["acceleration"]
     
     x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)
     
     
     #Linear Regression model on this dataset
     linear_model = LinearRegression().fit(x_train, y_train)
     linear_train_preds= linear_model.predict(x_train)
     test_preds=linear_model.predict(x_test)
     print("Mean value error with Linear Regression")
     print(mean_absolute_error(test_preds, y_test),mean_absolute_error(linear_train_preds, y_train))

    #Random Forest Regression model on this data set
     rf=RandomForestRegressor().fit(x_train, y_train)
     rf_train_preds = rf.predict(x_train)
     rf_test_preds = rf.predict(x_test)
     print("Mean value error with Random Forest Regression")
     print(mean_absolute_error(rf_train_preds, y_train), mean_absolute_error(rf_test_preds, y_test))

def acceleration(s):
    return np.round((s.loc['x']**2+s.loc['y']**2+s.loc['z']**2)**0.5,4)



if __name__=="__main__":
        
    print("___________________________________________________________")
    print("                      CSC 1302 Project                     ")
    print("___________________________________________________________")
    
    
    
    print("FIRST INPUT THE csv OR xlsx FILE FROM YOUR PC. ")
    opt1ch = int(input('''
          TYPE 1 AND ENTER TO CONFIRM (for csv file)
          TYPE 2 AND ENTER TO CONFIRM (for xlsx file) 
              : '''))
    if opt1ch == 1:
        while True:
            try:
                filename = input("ENTER THE FILENAME WITH .CSV EXTENSION: ")
                df = pd.read_csv(filename)
                print(df)
                # Create a new data frame with the rows with missing values dropped
                df = df.dropna()
                print("FILE RETRIVED AFTER DROPPING THE ROWS WITH NaN VAlues.")
                break
            except FileNotFoundError or ValueError:
                print("enter the correct file name")
                continue
            
    elif opt1ch == 2:
        while True:
            try:
                filename = input("ENTER THE FILENAME WITH .Xlsx EXTENSION: ")
                df = pd.read_excel(filename)
                print(df)
                # Create a new data frame with the rows with missing values dropped
                df = df.dropna()
                print("FILE RETRIVED AFTER DROPPING THE ROWS WITH NaN VAlues.")
                break
            except FileNotFoundError or ValueError:
                print("enter the correct file name")
                continue
    
   
    df['acceleration']=df.apply(acceleration,axis=1)  
    print("Adding a column of acceleration by finding the resultant of x,y,z")       
    print(df)
    
    mainmenu='''
     OPT.1. Manipulation
     OPT.2. Analysis
     OPT.3. Visualisation
     OPT 4. Machine Learning
     OPT.5. Exit'''
    print(mainmenu)
    
    userinput = int(input("ENTER YOUR CHOICE FROM THE MAIN MENU AND PRESS ENTER. "))
    
    if userinput == 1:
        manipulation(df)
    elif userinput ==2:
        analysis(df)
    elif userinput == 3:
        Visualisation(df)
    elif userinput ==4:
        test_train_data(df)
    if userinput == 5:
        print("BYE")


