# Project: Book My Show

class BookMyShow():
    def __init__(self,r,s):
        self.row=r
        self.seat=s
        self.SeatList=[]
        self.Price_of_seat=0
        self.TotalSeat=self.row * self.seat
        
        
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
            
    
class BuyTicket(BookMyShow):
    def __init__(self,R_seat,C_seat):
        self.R_seat=R_seat
        self.C_seat=C_seat 
        

    def ShowPriceOfSeat(self):
        
        if(self.TotalSeat<=60):
            self.Price_of_seat = 10
        
        if(self.TotalSeat>60):
            half=self.row//2             #row=main row number which enter by user in 1st time
        elif(self.R_seat<=half):
            self.Price_of_seat = 10
        else:
            self.Price_of_seat = 8
        print("Price of seat which you choice :  {} $".format(self.Price_of_seat))

    def check_vacant_seat(self):
        if(self.SeatList[self.R_seat][self.R_seat]=="B"):
            return False
        else:
            return True
        
        
    def Book_Ticket(self):
        check=self.check_vacant_seat()
        if(check):
            b.ShowPriceOfSeat(self.R_seat)
        else:
            return "This Seat is booked, please choose another"
        
        WantBuy=input("You Want to book seat then enter YES :")
        
        if(WantBuy.upper() == "YES"):
            self.SeatList[r][c]="B"
        
        return "Your seat is Booked"
    

 
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
        
        choice=int(input("You Choose : "))
        if(choice==1):
            b.show_seat()
        elif(choice==2):
            r=int(input("Enter thr row number for seat : "))
            c=int(input("Enter thr coloum number for seat : "))
            buy=BuyTicket(r,c)
            print(buy.Book_Ticket())
        elif(choice==0):
            Exit=0
        
        
            