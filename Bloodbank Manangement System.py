import pandas as pd


df= pd.read_csv("User_Profile.csv")
#print(df)
#print("=======================================")

df_columns=df.columns.tolist()

#print(df_columns)
#print("=======================================")
data_dict={}

for index,i in enumerate (df[df_columns[0]].tolist()):
    data_dict.update({i:[df[df_columns[1]][index],df[df_columns[2]][index],df[df_columns[3]][index]]})
#print(data_dict)
#print("=======================================")

        


def donating():
    bloodgroup=input("Enter the blood gr type:")
    for items in data_dict:
        while True:
            if bloodgroup in data_dict.keys():
                print("=======================================")
                bottles=input("Press\n1-To get 500ml\n2-To get 250ml\n")
                print("=======================================")
   #Checking Bottles
                if bottles=='1':
                    print("=======================================")
                    print("We have",data_dict[bloodgroup][1:2],"Bottles left")
                    print("=======================================")
                elif bottles=='2':
                    print("=======================================")
                    print("We have :",data_dict[bloodgroup][:1],"Bottles left")   
                    #print(total_bottles)
                    print("=======================================")
                    
                total_bottles1=data_dict[bloodgroup][1]
                total_bottles2=data_dict[bloodgroup][0]
                no_bottles=int(input("No of bottles you want :"))
    #Updating bottles
                if bottles=='1':
                    if no_bottles<=total_bottles1:
                        print("Blood transfered Successfully")
                        print("=======================================")
                        data_dict[bloodgroup][1]=int(data_dict[bloodgroup][1])-no_bottles
                        data_dict.update
                    else:
                        print("We don't have enough bottles")
                        print("=======================================")
                elif bottles=='2':
                     if no_bottles<=total_bottles2:
                        print("Blood transfered Successfully")
                        print("=======================================")
                        print()
                        data_dict[bloodgroup][0]=int(data_dict[bloodgroup][0])-no_bottles
                        data_dict.update
                     else:
                        print("We don't have enough bottles")
                        print("=======================================")
            break
        break


def receiving():
    bloodgroup=input("The Blood Group You want to donate :")
    print("=======================================")
    while True:
        if bloodgroup in data_dict.keys():
            bottles=input("Press\n1-To donate 500ml\n2-To donate 250ml\n")
   #Checking Bottles
            if bottles=='1':
                print("=======================================")
                print("We have",int(data_dict[bloodgroup][1])+1,"Bottles now")
                data_dict[bloodgroup][1]=int(data_dict[bloodgroup][1])+1
                data_dict.update
                print("=======================================")
            elif bottles=='2':
                print("=======================================")
                print("We have:",int(data_dict[bloodgroup][0])+1,"Bottles now")
                data_dict[bloodgroup][0]=int(data_dict[bloodgroup][0])+1
                data_dict.update
                    #print(total_bottles)
                print("=======================================")
        break



    


                    
def dataframe_list(index):
    arr=[]
    #print(index,"+")
    for i in data_dict:
        
        arr.append(data_dict[i][index])

    return arr
        

def update_data():
    updated_dict={}
    col=df_columns
    #print(col)
    updated_dict.update({col[0]:data_dict.keys()})
    col.pop(0)
    #print(col)
    for i,key in enumerate(col):
        updated_dict.update({key:dataframe_list(i)})
    dataframe=pd.DataFrame(updated_dict)
    print(dataframe)
    
    dataframe.to_csv("User_Profile.csv",index=False)

    

#donating()
#receiving()

while True:
    print("==========Welcome to Ehsaas Bank System==========\n")
    start_up_action=input("Press\n1-To donate Blood\n2-To Receive Blood\n3-To exit\n")
    print("=======================================")
    if start_up_action=="1":
        receiving()
    elif start_up_action=='2':
        donating()
    elif start_up_action=='3':
        update_data()
        print("=======================================")
        print("Window Exits")
        break
    else:
        print("Wrong input")
        print("=====================================================")
    
    

        


        
        
                
