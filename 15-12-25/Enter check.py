hour=int(input("Entry hour time:"))
min=int(input("Entry min time:"))
min=min+hour*60
if(min<540):
    print("Early entry: ENTERED BEFORE 9AM")
elif(min==540):
    print("On time entry: ENTERED AT 9AM")
else:
    print("Late entry: ENTERED AFTER 9AM")