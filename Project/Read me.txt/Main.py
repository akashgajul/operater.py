Project Name: Write a program to generate console base invoice
             -Add products with price 
             -show product list
             -generate invoice (Bills)

Group Members: Rohan Mushan    -     Presentation and Collected Data
               Utkarsh Gaikwad -     He Did Coding 
               Lokesh Alli     -     He also contributed on coding 
               Akash gajul     -     He collocted data and at the end he executed the Program
               Krishna Mhetre  -     krishna givened us the idea of this program and Helped i coding and 
                                     He Collocted RAW data and.   


#module mane: main
import read
import purchase
import write
again="Y"
while again.upper()=="Y":
    a=read.read_file()
    b=purchase.purchase(a)
    write.over_write(a,b)
    again=input("\nDoes the any new customer waiting to buy product? ")
print("\nThank you for shopping from our store!!")
print("Please check your invoice for your shopping details, \nWhich we created txt file format for you.")
                                  
