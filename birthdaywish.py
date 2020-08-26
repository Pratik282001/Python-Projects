import pandas as pd
import datetime
import smtplib
import os

os.chdir(r'D:\python projects')
os.mkdir('testing')

# Enter your authentication details
GMAIL_ID = '#'
GMAIL_PSWD = '#'

def sendmail(to, sub, msg):
    print(f'Sending Email to {to}')
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(GMAIL_ID, GMAIL_PSWD)
    s.sendmail(GMAIL_ID, to, f"Subject: {sub}\n\n{msg}")
    s.quit()


if __name__ == "__main__":
    df = pd.read_excel('Book1.xlsx')
    
    today = datetime.datetime.now().strftime("%d-%m")    
    YearNow = datetime.datetime.now().strftime("%y")    
    # print(today) prints today's date
    writeInd=[]
    
    for index, item in df.iterrows():
        
        x=str(item['year'])
        #print(index,item['birthday'])
        bday = item['birthday'].strftime("%d-%m")
        if(today==bday) and YearNow not in str(item['year']):
            sendmail(item['email'], "Happy Birthday", item['dialog'])
            writeInd.append(index)
    #print(writeInd)
    if(len(writeInd)==0):
        pass
    else:
        for i in writeInd:
            yr = df.loc[i, 'year']
            #print(yr)
            df.loc[i, 'year'] = str(yr) + ','+str(YearNow)
            #print(df.loc[i,'year'])
            
            
    df.to_excel('Book1.xlsx', index=False)