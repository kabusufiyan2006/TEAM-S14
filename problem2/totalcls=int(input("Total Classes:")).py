totalcls=int(input("Total Classes:"))
clsat=int(input("Classes Attended:"))
totper1=int((totalcls/100)*75)
stdper=int((clsat/totalcls)*100)
print("Attendence Percentage:",stdper,"%")
if(totper1<clsat):
    print("status:Eligible")
else:
    print("status:Not Eligible")
    totvalue=totper1-clsat
    print("Additnal classes Required:",totvalue)