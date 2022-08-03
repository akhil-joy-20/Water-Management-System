from ast import While
import xlwt
from xlwt import Workbook
import serial
Arduino = serial.Serial('COM4',9600)

wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')

#heading to excel sheet
sheet1.write(0, 0, 'Percentage')
sheet1.write(0, 1, 'Distance')
sheet1.write(0, 2, 'pH')
wb.save('data2.xls')

k=1;j=0;per=0;val=0;ph=0;r=1
ph_total=0

#***********************************************************************
# while True:
#   if (Arduino.inWaiting()>0):
#     myData = Arduino.readline()

#     x = myData.split()
#     ph = float(x[2])

    

#     print("PH: ",end=" ")
#     print(ph)

#     file3 = open('ph.txt', 'w')
#     file3.write(str(ph))

#     sheet1.write(1,2,str(ph))            
#     wb.save('data2.xls')  
#     break
    
# ph file
# ph_total/=8 #avg
# file0 = open('ph.txt', 'w')
# file0.write(str(ph))
# print(ph_total)

#****************************************************************************

while True:
    if (Arduino.inWaiting()>0):
        myData = Arduino.readline()

        x = myData.split()
        per=int(x[0])
        val=int(x[1])
        ph = float(x[2])

        if r==1:
            print("1")
            q=ph
            r+=1
        file3 = open('ph.txt', 'w')
        file3.write(str(q))
    
        print("PH: ",end=" ")
        print(ph)

        print("\nPercentage ",end=" ")
        print(per)
        
        print("Distance ",end=" ")
        print(val)

        sheet1.write(k,0,str(per))
        sheet1.write(k,1,str(val)) 
        sheet1.write(k,2,str(ph))
        wb.save('data2.xls')
        k=k+1   

        # percentage
        file2 = open('percent.txt', 'w')
        file2.write(str(per))

        # ph desc
        file1 = open('data.txt', 'w')
        if(q>=6.5)and(q<7):
            file1.write("Your Water is Acidic , however it is safe to drink.But it is not recommended to have water below pH level 6.5 for human uses, as it’s high acidity and concentration of heavy metals can have several negative health consequences such as decay of teeth enamel,shortness of breath etc")
        elif(q==7):
            file1.write("Your Water is at perfect state to drink,However this range is mostly unattainable due to the effect of organic agents and solvents")
        elif(q>7)and(q<8.5):
            file1.write("Your Water is slighty Alkaine but however it is safe to drink.It has benefits like immune system support,colon cleansing properties etc.Although drinking alkaline water is considered beneficial it has side effects like nausea,vomiting,hand tremors,muscle twitching etc")
        elif(q<6.5):
            file1.write("Escherichia Coli (E. Coli) or Salmonella Typhi (S. Typhi) might be present in your water. E. coli can cause mild to severe gastrointestinal illness. Some types of pathogenic (illness-causing) E. coli, such as Shiga toxin-producing E. coli (STEC), can be life-threatening.People infected with pathogenic E. coli can start to notice symptoms anywhere from a few days after consuming contaminated food or as much as nine days later. Generally, the symptoms include severe stomach cramps, diarrhea, fever, nausea, and/or vomiting.So if you find these symptoms, test your Water without taking risk")
        elif(q>8.5):
            file1.write("Your Water might contain Vibrio Cholera.Vibrio Cholera causes Cholera.The person who gets infected by this disease experiences severe watery diarrhea and this can lead to dehydration and even death if untreated. So if you upcome these syptoms please consult your doctor and also test your water quality ")
        else:
            file1.write("Your water is not safe to drink .Check it immediatly")
        file1.close()

        
       
# ***************************************************************************




