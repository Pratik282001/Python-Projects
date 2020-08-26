import pandas as pd
import datetime

def sendmail(to, sub, msg):
    print(f'Sending Email to {to}')


if __name__ == "__main__":
    df = pd.read_excel('Book1.xlsx')
    print("----------Birthday Database-------------")
    print(df) 
    today = datetime.datetime.now().strftime("%d-%m")    
    YearNow = datetime.datetime.now().strftime("%y")    
    # print(today) prints today's date
    writeInd=[]
    for index, item in df.iterrows():
        #print(index,item['birthday'])
        bday = item['birthday'].strftime("%d-%m")
        if(today==bday) and YearNow not in str(item['year']) :
            sendmail(item['email'], "Happy Birthday", item['dialog'])
            writeInd.append(index)
    print(writeInd)
    for i in writeInd:
        yr= df.loc[i, 'year']
        print(yr)