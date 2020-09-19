import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
def page(adminPage):
            def lightMode():
                adminPage.config(bg="white")
                AzPetrolLabel2.config(bg="white")
                errorLabel.config(bg="white")
            def darkMode():
                adminPage.config(bg="gray15")
                AzPetrolLabel2.config(bg="gray15")
                errorLabel.config(bg="gray15")
            def fuelPrice(event=None):
                fuel=typeVar.get()
                if fuel in fuelPriceDic.keys():
                    pricePerLiterLabel.config(text="Price Per L: "+str(fuelPriceDic[fuel])+" AZN")
            def getData():
                fuelOrPrice=var.get()
                if(fuelOrPrice==0):
                    literEntry.config(state="normal")
                    aznEntry.config(state="disabled")
                elif(fuelOrPrice==1):
                    aznEntry.config(state="normal")
                    literEntry.config(state="disabled")
                else:
                    literEntry.config(state="disabled")
                    aznEntry.config(state="disabled")

            def fuelTotal(event=None):
                fuel_price=var.get()
                try:
                    if(fuel_price==0):
                        liter=literEntry.get()
                        if(str(liter).isalpha()==True or float(liter)<0):
                            raise Exception("Liter value needs to be only digits and positive")
                        priceL=0
                        fuelP=typeVar.get()
                        priceL=float(liter)*fuelPriceDic[fuelP]
                        totalFuelPriceLabel.config(text="Total Fuel Price: "+str(priceL)+" AZN")
                        return priceL

                    elif(fuel_price==1):
                        enteredPrice=aznEntry.get()
                        if(str(enteredPrice).isalpha()==True or float(enteredPrice)<0):
                            raise Exception("Price needs to be only digits and positive")
                        totalFuelPriceLabel.config(text="Total Fuel Price: "+str(enteredPrice)+" AZN")
                        return enteredPrice
                    else:
                        return 0
                except Exception as ex:
                    messagebox.showerror(title="Error",message=ex)
            def fuelClear():
                var.set(2)
                fuelTypesComboBox.set("")
                pricePerLiterLabel.config(text="Price Per L:")
                literEntry.config(state="normal")
                aznEntry.config(state="normal")
                literEntry.delete(0,"end")
                aznEntry.delete(0,"end")
                totalFuelPriceLabel.config(text="Total Fuel Price: 0 AZN")
                getData()
            def foodClear():
                hotVar.set(0)
                
                hamVar.set(0)
                
                friVar.set(0)
                
                cokeVar.set(0)
                hotDogAmountEntry.delete(0,"end")
                hamburgerAmountEntry.delete(0,"end")
                friesAmountEntry.delete(0,"end")
                cokeAmountEntry.delete(0,"end")

                foodCalc(event=None)
            
                


            def foodCalc(event=None):
                hotDog=hotVar.get()
                hamburger=hamVar.get()
                fries=friVar.get()
                coke=cokeVar.get()
                
        
                try:
                    if( hotDog==1):
                        hotDogAmountEntry.config(state="normal")
                        hotDogAmount=hotDogAmountEntry.get()
                        if(hotDogAmount==""):
                            hotDogAmountEntry.insert(0,"0")
                            hotDogTotal=0
                        elif(str(hotDogAmount).isdigit()==True and float(hotDogAmount)>=0):
                            hotDogTotal=float(hotDogAmount)*4

                        else:
                            raise Exception("Hot Dog amount must be digits and positive")
                    else:
                        hotDogAmountEntry.config(state="disabled")
                        hotDogTotal=0
                    if hamburger==1:
                        hamburgerAmountEntry.config(state="normal")
                        hamburgerAmount=hamburgerAmountEntry.get()
                        if(hamburgerAmount==""):
                            hamburgerAmountEntry.insert(0,"0")
                            hamburgerTotal=0
                        elif(str(hamburgerAmount).isdigit()==True and float(hamburger)>=0):
                            hamburgerTotal=float(hamburgerAmount)*5.4
                        else:
                            raise Exception("Hamburger amount must be digits and positive")
                    else:
                        hamburgerAmountEntry.config(state="disabled")
                        hamburgerTotal=0

                    if( fries==1):
                        friesAmountEntry.config(state="normal")
                        friesAmount=friesAmountEntry.get()
                        if(friesAmount==""):
                            friesAmountEntry.insert(0,"0")
                            friesTotal=0
                        elif(str(friesAmount).isdigit()==True and float(friesAmount)>=0):
                            friesTotal=float(friesAmount)*3
                        else:
                            raise Exception("Fries amount must be digits and positive")
                    else:
                        friesAmountEntry.config(state="disabled")
                        friesTotal=0

                    if( coke==1):
                        cokeAmountEntry.config(state="normal")
                        cokeAmount=cokeAmountEntry.get()
                        if(cokeAmount==""):
                            cokeAmountEntry.insert(0,"0")
                            cokeTotal=0
                        elif(str(cokeAmount).isdigit()==True and float(cokeAmount)>=0):
                            cokeTotal=float(cokeAmount)*2
                        else:
                            raise Exception("Coke amount must be digits and positive")
                    else:
                        cokeAmountEntry.config(state="disabled")
                        cokeTotal=0
                    totalFoodPrice=hotDogTotal+hamburgerTotal+friesTotal+cokeTotal
                    
                    totalFoodLabel.config(text="Total Food Price: "+str(totalFoodPrice)+" AZN")
                    return totalFoodPrice

                        
                        
                except Exception as ex:
                    messagebox.showerror(title="Error",message=ex)
            def calculateAll():
                hotDog1=hotVar.get()
                hamburger1=hamVar.get()
                fries1=friVar.get()
                coke1=cokeVar.get()
                hotDogAmount1=hotDogAmountEntry.get()
                hamburgerAmount1=hamburgerAmountEntry.get()
                friesAmount1=friesAmountEntry.get()
                cokeAmount1=cokeAmountEntry.get()
                fuel_price=var.get()
            

                price1=fuelTotal(event=None)
                price2=foodCalc(event=None)

                if(str(price1).isalpha()==False and str(price2).isalpha()==False ):
                    total=float(price1)+float(price2)
                    totalPrice.config(text=total)
                import random
                from datetime import datetime
                timestamp=datetime.timestamp(datetime.now())
                filename="check"+str(random.randrange(10000,1000000))+str(timestamp)+".txt"
                file=open("C:\\Users\\Sanan\\Desktop\\"+filename,"w",encoding="utf-8")
                file.write("\n\n")
                file.write("         AZPETROL")
                file.write("\n\n\n")
                date=datetime.now()
                file.write(f"Date: {str(date)[:19]}")

                file.write("\n\n\n")
                file.write("Product   Amount    Price\n")
                file.write("___________________________")
                file.write("\n")
                isTrue=True
                allStatements=[]
                
                if(hotDog1==1):
                    if(str(hotDogAmount1).isalpha()==False):
                        if(int(hotDogAmount1)>0):
                            file.write("HotDog"+" "*6+hotDogAmount1+" "*(8-len(hotDogAmount1))+str(float(int(hotDogAmount1)*4))+ " AZN"+"\n")
                    else:
                        isTrue=False
                        allStatements.append(isTrue)
             
                    
                if(hamburger1==1):
                    if(str(hamburgerAmount1.isalpha()==False)):    
                        if(int(hamburgerAmount1)>0):
                            file.write("Hamburger"+" "*3+hamburgerAmount1+" "*(8-len(hamburgerAmount1))+str(float(int(hamburgerAmount1)*5.4)) + " AZN"+"\n")
                    else:
                        isTrue=False
                        allStatements.append(isTrue)

    
                if(fries1==1):
                    if(str(friesAmount1.isalpha()==False)):   
                        if(int(friesAmount1)>0):
                            file.write("Fries"+" "*7+friesAmount1+" "*(8-len(friesAmount1))+str(float(int(friesAmount1)*3))+" AZN"+"\n")
                    else:
                        isTrue=False
                        allStatements.append(isTrue)
                

                if(coke1==1):
                    if(str(cokeAmount1.isalpha()==False)):   
                        if(int(cokeAmount1)>0):
                            file.write("Coke"+" "*8+cokeAmount1+" "*(8-len(cokeAmount1))+str(float(int(cokeAmount1)*2))+" AZN"+"\n")
                    else:
                        isTrue=False
                        allStatements.append(isTrue)
                
        
                if(fuel_price==0):
                    liter=literEntry.get()
                    if(str(liter).isalpha()==False and float(liter)>0):
                        fuelP=typeVar.get()
                        priceL=float(liter)*fuelPriceDic[fuelP]
                        file.write(str(fuelP)+" "*(12-len(fuelP))+str(liter)+"L"+" "*(7-len(liter))+ str(priceL) +" AZN"+"\n")
                    else:
                       
                        isTrue=False
                        allStatements.append(isTrue)
                    

               
                
                if(fuel_price==1):
                    enteredPrice=aznEntry.get()
                    if(str(enteredPrice).isalpha()==False and float(enteredPrice)>0):
                        fuelP=typeVar.get()
                        litres=float(enteredPrice)/fuelPriceDic[fuelP]
                        file.write(str(fuelP)+" "*(12-len(fuelP))+str(litres)+"L "+" "*(7-len(str(litres)))+str(enteredPrice) +" AZN"+"\n")
                    else:
                        isTrue=False
                        allStatements.append(isTrue)
                
                if(False in allStatements):
                    pass
                else:
                    file.write("__________________________\n")
                    file.write("Total: "+" "*13+str(total)+" AZN\n")
                    file.write("__________________________\n")
                    file.write("Thank you for shopping with us!")
                    file.close()
                    calculateButton.config(state="disabled")



    
            def fullClear():
                foodClear()
                fuelClear()
                totalPrice.config(text="0.0")
                calculateButton.config(state="normal")
            def getfuelTypes():
                newTypes=fuelTypes
                return fuelTypes


            typeVar=tk.StringVar()
            adminPage.config(bg="white")
            adminPage.resizable(False,False)
            adminPage.geometry("1000x750")
            adminPage.title("AzPetrol Admin Page")
            adminPage.iconbitmap("Azpetrol_logo.ico")
            AzPetrolLabel2=tk.Label(adminPage,image=AzPetrolPhoto,bg="white")
            AzPetrolLabel2.place(x=450,y=0)
            petrolFrame=tk.Frame(adminPage, width=400, height=400, bg="green")
            petrolFrame.place(x=50,y=150)
            gasolineLabel=tk.Label(adminPage,text="Gasoline Station",font=("Times",15,"bold"),bg="green")
            gasolineLabel.place(x=50,y=150)
            menuFrame=tk.Frame(adminPage,width=400,height=400,bg="green")
            menuFrame.place(x=550,y=150)
            errorLabel=tk.Label(adminPage,text="",font=("Times",20,"bold"),fg="red",bg="white")
            errorLabel.place(x=50,y=50)
            allPriceFrame=tk.Frame(adminPage,width=900,height=150,bg="green")
            allPriceFrame.place(x=50,y=570)
            fuelLabel=tk.Label(adminPage,text="Fuel Type:",font=("Times",20,"bold"),bg="green")
            fuelLabel.place(x=50,y=200)



            fuelTypesComboBox=Combobox(adminPage,font=("Times",20,"bold"),values=getfuelTypes(),width=15,textvariable=typeVar)
            fuelTypesComboBox.bind("<<ComboboxSelected>>",fuelPrice)
            fuelTypesComboBox.place(x=200,y=200)
            pricePerLiterLabel=tk.Label(adminPage,text="Price Per L:",font=("Times",20,"bold"),bg="green")
            pricePerLiterLabel.place(x=50,y=250)
            var=tk.IntVar()
            var.set(2)
            literRadiobutton=tk.Radiobutton(adminPage,text="Liter:",variable=var,value=0,bg="green",font=("Times",20,"bold"),command=getData)
            literRadiobutton.place(x=50,y=300)
            literEntry=tk.Entry(adminPage,font=("Times",20,"bold"),state="disabled",width=15)
            literEntry.place(x=200,y=300)
            literEntry.bind("<Return>",fuelTotal)
            aznRadiobutton=tk.Radiobutton(adminPage,text="Price:",variable=var,value=1,bg="green",font=("Times",20,"bold"),command=getData)
            aznRadiobutton.place(x=50,y=350)
            aznEntry=tk.Entry(adminPage,font=("Times",20,"bold"),state="disabled",width=15)
            aznEntry.place(x=200,y=350)
            aznEntry.bind("<Return>",fuelTotal)
            totalFuelPriceLabel=tk.Label(adminPage,text="Total Fuel Price: 0 AZN",font=("Times",20,"bold"),bg="green")
            totalFuelPriceLabel.place(x=50,y=400)
            fuelClearButton=tk.Button(adminPage,text="Clear All",font=("Times",20,"bold"),bg="green",command=fuelClear)
            fuelClearButton.place(x=190,y=480)
            minicafeLabel=tk.Label(adminPage,text="Mini Cafe",font=("Times",15,"bold"),bg="green")
            minicafeLabel.place(x=550,y=150)
            hotVar=tk.IntVar()
            hotVar.set(0)
            hamVar=tk.IntVar()
            hamVar.set(0)
            friVar=tk.IntVar()
            friVar.set(0)
            cokeVar=tk.IntVar()
            cokeVar.set(0)
            
            hotDogCheckBox=tk.Checkbutton(adminPage,text="Hot Dog",variable=hotVar,font=("Times",20,"bold"),bg="green",command=foodCalc)
            hotDogCheckBox.place(x=550,y=200)
            hotDogPriceLabel=tk.Label(adminPage,text="4.00",font=("Times",20,"bold"))
            hotDogPriceLabel.place(x=700,y=200)
            hotDogAmountEntry=tk.Entry(adminPage,font=("Times",20,"bold"),state="disabled",width=10)
            hotDogAmountEntry.insert(0,"0")
            hotDogAmountEntry.place(x=770,y=200)
            hotDogAmountEntry.bind("<Return>",foodCalc)

            hamburgerCheckBox=tk.Checkbutton(adminPage,text="Hamburger",variable=hamVar,font=("Times",20,"bold"),bg="green",command=foodCalc)
            hamburgerCheckBox.place(x=550,y=250)
            hamburgerPriceLabel=tk.Label(adminPage,text="5.40",font=("Times",20,"bold"))
            hamburgerPriceLabel.place(x=720,y=250)
            hamburgerAmountEntry=tk.Entry(adminPage,font=("Times",20,"bold"),state="disabled",width=10)
            hamburgerAmountEntry.place(x=790,y=250)
            hamburgerAmountEntry.bind("<Return>",foodCalc)

            friesCheckBox=tk.Checkbutton(adminPage,text="Fries",variable=friVar,font=("Times",20,"bold"),bg="green",command=foodCalc)
            friesCheckBox.place(x=550,y=300)
            friesPriceLabel=tk.Label(adminPage,text="3.00",font=("Times",20,"bold"))
            friesPriceLabel.place(x=720,y=300)
            friesAmountEntry=tk.Entry(adminPage,font=("Times",20,"bold"),state="disabled",width=10)
            friesAmountEntry.place(x=790,y=300)
            friesAmountEntry.bind("<Return>",foodCalc)

            cokeCheckBox=tk.Checkbutton(adminPage,text="Coke",variable=cokeVar,font=("Times",20,"bold"),bg="green",command=foodCalc)
            cokeCheckBox.place(x=550,y=350)
            cokePriceLabel=tk.Label(adminPage,text="2.00",font=("Times",20,"bold"))
            cokePriceLabel.place(x=720,y=350)
            cokeAmountEntry=tk.Entry(adminPage,font=("Times",20,"bold"),state="disabled",width=10)
            cokeAmountEntry.place(x=790,y=350)
            cokeAmountEntry.bind("<Return>",foodCalc)

            totalFoodLabel=tk.Label(adminPage,text="Total Food Price: 0 AZN",font=("Times",20,"bold"),bg="green")
            totalFoodLabel.place(x=550,y=400)
            
            foodClearButton=tk.Button(adminPage,text="Clear All",font=("Times",20,"bold"),bg="green",command=foodClear)
            foodClearButton.place(x=670,y=480)

            allpriceLabel=tk.Label(adminPage,text="All Price",font=("Times",20,"bold"),bg="green")
            allpriceLabel.place(x=50,y=570)

            calculateButton=tk.Button(adminPage,text="Calculate",font=("Times",20,"bold"),bg="white",command=calculateAll)
            calculateButton.place(x=220,y=630)
            deleteAllButton=tk.Button(adminPage,text="Delete All",font=("Times",20,"bold"),bg="white",command=fullClear)
            deleteAllButton.place(x=400,y=630)
            totalFrame=tk.Frame(adminPage,width=200,height=80,bg="white")
            totalFrame.place(x=670,y=630)
            aznLabel=tk.Label(adminPage,text="AZN",font=("Times",15,"bold"),bg="green")
            aznLabel.place(x=880,y=670)
            totalPrice=tk.Label(adminPage,text="0.0",font=("Times",20,"bold"),bg="white")
            totalPrice.place(x=670,y=630)

            

            lightModeButton=tk.Button(adminPage,text="Light Mode",font=("Times",20,"bold"),command=lightMode)
            lightModeButton.place(x=600,y=50)
            darkModeButton=tk.Button(adminPage,text="Dark Mode",font=("Times",20,"bold"),command=darkMode)
            darkModeButton.place(x=800,y=50)


login=tk.Tk()
def logIn():
    username=""
    password=""
    try:
        username=usernameEntry.get()
        password=passwordEntry.get()
    except Exception as ex:
        print("Left application")
    if(username.lower()=="sanan2003" and password=="12345"):
        def addNew():
            newFuel=fuelTypeEntry.get()
            newFuelPrice=newFuelPriceEntry.get()
            try:
                global fuelPriceDic
                if  str(newFuelPrice).isalpha()==False and str(newFuel)!="":
                    fuelTypes.append(newFuel)
                    fuelPriceDic[newFuel]=float(newFuelPrice)
                    
                    page(adminPage)
                    
                    
                else:
                    raise Exception("New Price must be digits")
            except Exception as ex:
                messagebox.showerror(title="Error",message=ex)
        adminPage=tk.Toplevel()
        newFuelType=tk.Label(adminPage,text="New Fuel Type and Price",font=("Times",12,"bold"),bg="white")
        newFuelType.place(x=50,y=50)
        fuelTypeEntry=tk.Entry(adminPage,font=("Times",12,"bold"),bg="white",width=10)
        fuelTypeEntry.place(x=250,y=50)
        newFuelPriceEntry=tk.Entry(adminPage,font=("Times",12,"bold"),bg="white",width=6)
        newFuelPriceEntry.place(x=350,y=50)
        addButton=tk.Button(adminPage,text="Add",font=("Times",15,"bold"),bg="white",command=addNew)
        addButton.place(x=150,y=100)
        page(adminPage)
        adminPage.mainloop()
    elif(username=="" and password==""):
        pass
    else:
        messagebox.showerror(title="Log In Error",message="Username Or Password Wrong,Please Try Again")
def guestMode():
    guestPage=tk.Toplevel()
    page(guestPage)
    guestPage.mainloop()

AzPetrolPhoto=tk.PhotoImage(file="azpetrol.gif")
AzPetrolLabel1=tk.Label(login,image=AzPetrolPhoto,bg="white")
AzPetrolLabel1.pack()
login.iconbitmap("Azpetrol_logo.ico")
login.title("AzPetrol Login")
login.config(bg="white")
login.geometry("500x500")
login.resizable(False,False)
usernameLabel=tk.Label(login,text="Username:",font=("Times",20,"bold"),bg="white")
usernameLabel.place(x=50,y=170)
usernameEntry=tk.Entry(login,font=("Times",20,"bold"),width=20)
usernameEntry.place(x=190,y=170)
passwordLabel=tk.Label(login,text="Password:",font=("Times",20,"bold"),bg="white")
passwordLabel.place(x=50,y=220)
passwordEntry=tk.Entry(login,font=("Times",20,"bold"),width=20)
passwordEntry.place(x=190,y=220)
loginButton=tk.Button(login,text="Log in",font=("Times",20,"bold"),command=logIn)
loginButton.place(x=50,y=350)
guestButton=tk.Button(login,text="Guest Mode",font=("Times",20,"bold"),command=guestMode)
guestButton.place(x=300,y=350)
fuelTypes=["A 92","Premium","Diesel","CNG Gas"]
fuelPriceDic={
                "A 92":0.9,
                "Premium":1.25,
                "Diesel":0.6,
                "CNG Gas":0.45
            }

login.mainloop()