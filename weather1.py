from tkinter import*
import requests
class MyWeather:
    def __init__(self,root):
        self.root=root
        self.root.title("Weather app")
        self.root.geometry("300x400")
        self.root.config(bg="white")
        # variable
        self.var_search=StringVar()

        title=Label(self.root,text="Weather app",font=("goudy old style",30,"bold"),bg="#728FCE",fg="white").place(x=0,y=0,relwidth=1)
        lbl_city=Label(self.root,text="City Name",font=("goudy old style",15,"bold"),bg="#00FFFF",fg="black",anchor="w").place(x=0,y=70,relwidth=1)
        txt_city=Entry(self.root,textvariable=self.var_search,font=("goudy old stystyle",15),bg="#C0C0C0",fg="black").place(x=100,y=70,width=150)
        but_city=Button(self.root,text="Search",font=("goudy old stystyle",15),bg="#F08080",fg="white",command=self.get_weather).place(x=80,y=110,width=150)

        #------------------reustls-----------------
        self.lbl_city=Label(self.root,text="City Name",font=("times new roman",15,"bold"),bg="white",fg="black",width=30)
        self.lbl_city.place(x=0,y=170,relwidth=1)

        self.lbl_temp=Label(self.root,text="Temperature",font=("times new roman",15,"bold"),bg="white",fg="black",width=30)
        self.lbl_temp.place(x=0,y=210,relwidth=1)

        self.lbl_humidity=Label(self.root,text="Humidity",font=("times new roman",15,"bold"),bg="white",fg="black",width=30)
        self.lbl_humidity.place(x=0,y=250,relwidth=1)

        self.lbl_error=Label(self.root,text="Error",font=("times new roman",15,"bold"),bg="white",fg="black",width=30)
        self.lbl_error.place(x=0,y=290,relwidth=1)

        #=====footer==
        lbl_footer=Label(self.root,bg="#ADF802")
        lbl_footer.pack(side=BOTTOM,fill=X)

        
    def get_weather(self):
        api_key="98caa50a8d34ff61897a1e1ace038378"
        api_url=f"http://api.openweathermap.org/data/2.5/weather?q={self.var_search.get()}&appid={api_key}"
        #city name,countryname ,temp_c temp_f,humidity
        if self.var_search.get()=="":
            self.lbl_error.config(text="city name required")
        else:    
            result=requests.get(api_url)
            if result:
                json=result.json()
                city_name=json["name"]
                country=json["sys"]["country"]
                temp_c=json["main"]["temp"]-273.15
                temp_f=(json["main"]["temp"]- 273.15)*9/5+32
                humidity=json["main"]["humidity"]
                self.lbl_city.config(text=city_name+", "+country)


                
                
                self.lbl_temp.config(text=str(round(temp_c,2))+"C ! "+str(round(temp_f,2))+"F")
                self.lbl_humidity.config(text=humidity)
                self.lbl_error.config(text=" ")

            else:
                self.lbl_city.config(text="")
                self.lbl_temp.config(text="")
                self.lbl_humidity.config(text="")
                self.lbl_error.config(text=" you not find this city name")
root=Tk()
obj=MyWeather(root)
root.mainloop()        