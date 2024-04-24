'''5)Write a Python program to convert a month name to a number of days.
Expected Output:

List of months: January, February, March, April, May, June, July, August
, September, October, November, December                                
Input the name of Month: February                                       
No. of days: 28/29 days'''

def days_in_month(month_name):
    months = {"January":31,"February":"28 / 29","March":31,"April":30,"May":31,"June":30,"July":31,"August":31,"September":30,"October":31,"November":30,"December":31}
    return months.get(month_name,"Invalid month")
def main():
    print("List of months:January, February, March, April, May, June, July, August, September, October, November, December")
    month_name=input("Month name:")
    days=days_in_month(month_name)
    print("Total days:",days,"days")
if __name__=="__main__":
    main()
    
    
    
    


