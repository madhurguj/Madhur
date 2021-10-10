# Project: Book My Show

''' Madhur Gujarathi'''

import re

class Ticket_info():
    def __init__(self,user):
        self.user=user
        
    def ticketbookseat(self):
        if(len(self.obj) ==0):
            print("Not singel Tickets booked Yet")
            return True
        else:
            for i in self.obj:
                print(i, end="  ")
        
    def get_info(self): 
    
        r=int(input("\nEnter thr row number of seat  : "))
        c=int(input("Enter thr coloum number of seat : "))
        arg=(r,c)
        
        if (arg in self.obj):
                
            a=self.obj[arg].user[arg]
            print("\nName: ",a["Name"])
            print("Gender: ",a["Gender"])
            print("Age: ",a["Age"])
            print("Ticket Price: ", a["Price"])
            print("Phone No. : ",a["Phone"])
            
        else:
            print("{} Seat is not book yet".format(arg))
            
    def set_name(self):
        while True:
            Name=input("Name : ")
            if(re.search("^[A-Za-z ]*$", Name)):
                return Name
                break
            print("Please enter Valid name")
        
    def set_gender(self):
        while True:
            Gender=input("Gender : ")
            if(re.search("[mM]ale|[fF]emale|^[fF]$|^[mM]$", Gender)):
                return Gender
                break
            print("Please enter Valid Gender")
    
    def set_age(self):
        while True:
            Age=input("Age : ")
            if(re.search("^\d{1,2}$", Age)):
                return Age
                break
            print("Please enter Valid Age")
            
    def set_phone(self):
        while True:
            Phone=input("Phone No. : ")
            if(re.search("^\d{10}$", Phone)):
                return Phone
                break
            print("Please enter 10 Digit Phone number")
            
            
class statistics():
        
    def statistics(self):
        print("\nNumber of purchased tickets: ",BookMyShow.count)
        print("Percentage: {}%".format(round((BookMyShow.count/self.TotalSeat)*100,2)))
        print("Current income: ${}".format(self.current_income))
        print("Toatl income: ${}".format(self.Total_income))

    
    
class BookTicket():
    def __init__(self,rs,cs):
        self.R_seat=rs
        self.C_seat=cs
        
    def ShowPriceOfSeat(self):
        if(self.TotalSeat<=60):
            self.Price_of_seat = 10
            self.Total_income=self.TotalSeat*10
        elif(self.TotalSeat>60):
            half=self.row//2                         #row=main row number which enter by user in 1st time
            if(self.R_seat<=half):
                self.Price_of_seat = 10
            else:
                self.Price_of_seat = 8
                
            self.Total_income=half*self.seat*10 + (self.row-half)*self.seat*8
        print("Price of seat which you choice :  ${}".format(self.Price_of_seat))
        self.current_income+=self.Price_of_seat
 
    
    def check_vacant_seat(self,):
        if(self.SeatList[self.R_seat][self.C_seat]=="B"):
            return False
        else:
            return True
           
    
    def Book_Ticket(self,R_seat,C_seat):
        BookTicket.__init__(self,R_seat,C_seat)
        check=self.check_vacant_seat()
        if(check):
            self.ShowPriceOfSeat()
        else:
            return "This Seat is booked, please choose another"
        
        WantBuy=input("You Want to book seat then enter YES :")
        
        if(WantBuy.upper() == "YES" or WantBuy.upper()=="Y"):
            user={}
            Name=b.set_name()
            Gender=b.set_gender()
            Age =b.set_age()
            Phone =b.set_phone()
            d={"Name" :Name , "Gender" : Gender, "Age" :Age,"Price":self.Price_of_seat, "Phone": Phone}
            user[(R_seat,C_seat)]=d
            i=Ticket_info(user)
            self.obj[(R_seat,C_seat)]=i
            self.SeatList[r][c]="B"
            BookMyShow.count+=1
        else:
            return "\nYou Not Book Ticket"
        
        return "\nBooked Succesfully"
    
        
    
class BookMyShow(BookTicket,statistics,Ticket_info):
    count=0
    def __init__(self,r,s):
        self.row=r
        self.seat=s
        self.SeatList=[]
        self.current_income=0
        self.Total_income=0
        self.Price_of_seat=0
        self.TotalSeat=self.row * self.seat
        self.obj={}
        
    def Total_Seat(self):
        self.TotalSeat=self.row*self.seat
        
        
    def seat_list(self):
        for i in range(self.row+1):
            row=[]
            for j in range(self.seat+1):
                if(i==0 and j==0 ):
                    row.append(" ")
                elif(i==0):
                    row.append(j)
                elif(j==0):
                    row.append(i)
                else:
                    row.append("S")
            self.SeatList.append(row)
        
 
    def show_seat(self):
        print("\nCinema: ")
        for i in range(self.row+1):
            for j in range(self.seat+1):
                print(self.SeatList[i][j], end=" ")
            print()
            

    
    
    


if __name__ == "__main__":
    
    row=int(input("Enter the number of row :\n"))
    seat=int(input("Enter the number of seat in each row :\n"))
    b=BookMyShow(row,seat)
    b.seat_list()
    
    Exit=1
    while(Exit!=0):
        print("\n1. Show the seats")
        print("2. Buy a Ticket")
        print("3. Statistics")
        print("4. Show booked Tickets User Info")
        print("0. Exit\n")
        try:
            choice=int(input("Choose the option from above : "))
              
            if(choice==1):
                b.show_seat()
            elif(choice==2):
                r=int(input("Enter thr row number for seat : "))
                c=int(input("Enter thr coloum number for seat : "))
                if(r>row or c>seat or r<=0 or c<=0):
                    print("\nThis seat is not available.  Please choose correct seat from below.\n")
                    b.show_seat()
                else:
                    print(b.Book_Ticket(r,c))
            elif(choice==3):
                b.statistics()
            elif(choice==4):
                d=b.ticketbookseat()
                if(d!=True):
                    b.get_info()
            elif(choice==0):
                print("\nEnjoy!!")
                Exit=0
            elif(0<choice>3 ):
                print("\nChoose correct option from below.")
            
        except:
            print("\nPlease Enter Valid Input")
          
            