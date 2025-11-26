from tkinter import *
try:
    from PIL import Image, ImageTk
except Exception:
    Image = None
import pymysql


root = Tk()
root.title("Airline Reservation System")
# Keep the app initially fullscreen; we'll provide a toggle for fullscreen (maximize) in-app
root.attributes('-fullscreen', True)
is_fullscreen = [True]  # mutable container so nested functions can modify
_bg_path = (r"/home/m4verick/Downloads/istockphoto-1714990127-612x612.jpg")
# _bg_path = r"/home/m4verick/Downloads/istockphoto-1714990127-612x612.jpg"  # Path to my background image
try:
    bg = PhotoImage(file=_bg_path)
except Exception:
    if Image is not None:
        try:
            img = Image.open(_bg_path)
            bg = ImageTk.PhotoImage(img)
        except Exception:
            bg = None
    else:
        bg = None
   
canvas1 = Canvas( root, width = 1500, 
                 height = 550)
canvas1.pack(fill = "both", expand = True)
 
if bg is not None:
    canvas1.create_image( 0, 0, image = bg, 
                         anchor = "nw")
    def minimize_app():
        root.iconify()

    def toggle_maximize():
        # Toggle the fullscreen attribute
        is_fullscreen[0] = not is_fullscreen[0]
        root.attributes('-fullscreen', is_fullscreen[0])

    def close_app():
        root.destroy()

    controls_frame = Frame(root, bg=None)
    controls_frame.place(relx=0.98, rely=0.02, anchor='ne')

    min_btn = Button(controls_frame, text="_", width=3, command=minimize_app, bg="lightgrey")
    max_btn = Button(controls_frame, text="▢", width=3, command=toggle_maximize, bg="lightgrey")
    close_btn = Button(controls_frame, text="✕", width=3, command=close_app, bg="#ff4d4d")
    min_btn.pack(side="left", padx=(0,4))
    max_btn.pack(side="left", padx=(0,4))
    close_btn.pack(side="left")


def passenger():

    master = Tk()
    master.geometry("1000x500")
    master.title( "Air Reservation System" )    
    

    
    textName = StringVar()
    textDob = StringVar()
    textPassNum = StringVar()
    textPassId = StringVar()

    Label(master, text="Name: ").grid(row=0)
    Label(master, text="Date Of Birth: ").grid(row=1)
    Label(master, text="Phone Number: ").grid(row=2)
    Label(master, text="Passenger I.D.: ").grid(row=3)

    Label(master, text="(Example of Name input: Shubham )").grid(row=15)
    Label(master, text="(Example of Date Of Birth input: 2007-09-18) ").grid(row=16)
    Label(master, text="(Example of Phone Number input: 98xxxxx779) ").grid(row=17)
    Label(master, text="(Example of Passenger I.D. input: 1234)").grid(row=18)
    

    name = Entry(master, textvariable=textName)
    dob = Entry(master, textvariable=textDob)
    passNum = Entry(master, textvariable=textPassNum)
    passId = Entry(master, textvariable = textPassId)
    def done():



        texta = "{}".format(name.get())
        textb = "{}".format(dob.get())
        textc = "{}".format(passNum.get())
        textd = "{}".format(passId.get())
        print(texta)

        dataa = (texta, textb, textc, textd)
        print(dataa)
        db = pymysql.connect(host='localhost', user='root', password='Shubhh@95298', database='Air_Reservation', autocommit=True)
        cursor = db.cursor()
        '''Mysql for user input'''

        cursor.execute("INSERT INTO Passenger VALUES (%s, %s, %s, %s)", dataa)
        db.commit()
        print(cursor.fetchall())

        db.close()

        #print('"{}"'.format(name.get()))
       # print(texta)

    def deletePassenger():
        deletePass = Tk()
        deletePass.geometry("1400x440")
        deletePass.title("Air Reservation System")

        deletePassInput = StringVar()

        Label(deletePass, text="Passenger Number: ").grid(row=0)
        Label(deletePass, text="You have to know your Passenger Number to delete your passenger data").grid(row=1)
        Label(deletePass, text="(Example of Passenger Number: 1122334455) ").grid(row=2)

        passDelete = Entry(deletePass, textvariable=deletePassInput)
        passDelete.grid(row=0, column=1)

        def delete():
            texta = "{}".format(passDelete.get())
            print(texta)
            dataa = (texta)
            print(dataa)

            dataa = (texta,)
            print(dataa)

            db = pymysql.connect(host='localhost', user='root', password='Shubhh@95298', database='Air_Reservation', autocommit=True)
            cursor = db.cursor()
            '''Mysql for user input'''

            cursor.execute("DELETE FROM Passenger WHERE passNum=%s", dataa)
            cursor.execute("SELECT * FROM Passenger;")
            print(cursor.fetchall())

            db.close()

        Buttonh = Button(deletePass, text="Save", command=delete).place(x=20, y=150)


        
    Buttong = Button(master, text="Delete Passenger", command=deletePassenger).place(x=20, y=330)
    Button(master, text="Save", command=done).place(x=20, y=300)
    name.grid(row=0, column=1)
    dob.grid(row=1, column=1)
    passNum.grid(row=2, column=1)
    passId.grid(row=3, column=1)











def ticket():

    master = Tk()
    master.geometry("1000x500")
    master.title("Air Reservation System")

    textTicketNum = StringVar()
    textSeatNum = StringVar()

    Label(master, text="Ticket Number: ").grid(row=0)
    Label(master, text="Seat Number: ").grid(row=1)

    Label(master, text="(Example of Ticket Number input: 11220)").grid(row=15)
    Label(master, text="(Example of Seat Number input: 100) ").grid(row=16)

#Change seat number

    ticketNum = Entry(master, textvariable=textTicketNum)
    seatNum = Entry(master, textvariable=textSeatNum)
    ticketNum.grid(row=0, column=1)
    seatNum.grid(row=1, column=1)



    def done():



        texta = "{}".format(ticketNum.get())
        textb = "{}".format(seatNum.get())

        print(texta)

        dataa = (texta, textb)
        print(dataa)

        dataa = (texta, textb)
        print(dataa)


        db = pymysql.connect(host='localhost', user='root', password='Shubhh@95298', database='Air_Reservation', autocommit=True)
        cursor = db.cursor()
        '''Mysql for user input'''

        cursor.execute("INSERT INTO Ticket VALUES (%s, %s)", dataa)
        db.commit()

        cursor.execute("""SELECT * FROM Ticket;""")
        print(cursor.fetchall())

        db.close()






    def deleteTicket():


        deleteTick = Tk()
        deleteTick.geometry("900x440")
        deleteTick.title("Air Reservation System")

        deleteTickInput = StringVar()

        Label(deleteTick, text="Ticket Number: ").grid(row=0)

        Label(deleteTick, text="Example of Ticket Number: 11220 ").grid(row=1)

        ticketDelete = Entry(deleteTick, textvariable=deleteTickInput)
        ticketDelete.grid(row=0, column=1)
        def delete():


            texta = "{}".format(ticketDelete.get())
            print(texta)
            dataa = (texta)
            print(dataa)

            db = pymysql.connect(host='localhost', user='root', passwd='Shubhh@95298', db='Air_Reservation',
                                     autocommit=True)

            cursor = db.cursor()

            '''Mysql for user input'''

            cursor.execute("DELETE FROM Ticket WHERE ticketNum=%s", dataa)
            cursor.execute("""SELECT * FROM Ticket;""")

            print(cursor.fetchall())

            db.close()


        Buttonf = Button(deleteTick, text="Save", command=delete).place(x=20, y=150)

    Button(master, text="Save", command=done).place(x=20, y=150)
    Button(master, text="Delete Ticket", command=deleteTicket).place(x=20, y=180)
    








def flight():

    master = Tk()
    master.geometry("1000x500")
    master.title("Air Reservation System")

    textFlightId = StringVar()
    textFlightTerm = StringVar()
    textFlighTicket = StringVar()
    textNumFlights = StringVar()

    Label(master, text="Flight I.D.: ").grid(row=0)
    Label(master, text="Flight Terminal: ").grid(row=1)
    Label(master, text="Flight Ticket: ").grid(row=2)
    Label(master, text="Number of Flights: ").grid(row=3)

    Label(master, text="(Example of Flight I.D.: 1001) ").grid(row=15)
    Label(master, text="(Example of Flight Terminal: A-1) ").grid(row=16)
    Label(master, text="(Example of Flight Ticket: 1)  ").grid(row=17)
    Label(master, text="(Example of Number of Flights: 1) ").grid(row=18)
    Message(master, text="*** In order to change flight information, you must delete it using your flight I.D. number and then insert another one***", width = 200).grid(row=19)


    flightId = Entry(master, textvariable=textFlightId)
    flightTerm = Entry(master, textvariable=textFlightTerm)
    flightTicket = Entry(master, textvariable=textFlighTicket)
    numFlights = Entry(master, textvariable=textNumFlights)
    def done():



        texta = "{}".format(flightId.get())
        textb = "{}".format(flightTerm.get())
        textc = "{}".format(flightTicket.get())
        textd = "{}".format(numFlights.get())
        print(texta)

        dataa = (texta, textb, textc, textd)
        print(dataa)
        db = pymysql.connect(host='localhost', user='root', passwd='Shubhh@95298', db='Air_Reservation', autocommit=True)
        cursor = db.cursor()

        '''Mysql for user input'''

        cursor.execute("INSERT INTO Flight VALUES (%s, %s, %s, %s)", dataa)
        db.commit()

        print(cursor.fetchall())

        db.close()

        #print('"{}"'.format(name.get()))
       # print(texta)

    def deleteFlight():
        deleteFli = Tk()
        deleteFli.geometry("1400x440")
        deleteFli.title("Air Reservation System")

        deleteFliInput = StringVar()

        Label(deleteFli, text="Passenger Number: ").grid(row=0)
        Label(deleteFli, text="You have to know your Flight I.D. to delete your flight data").grid(row=1)
        Label(deleteFli, text="Example of Passenger Number: 1122334455 ").grid(row=2)

        fliDelete = Entry(deleteFli, textvariable=deleteFliInput)
        fliDelete.grid(row=0, column=1)

        def delete():
            texta = "{}".format(fliDelete.get())
            print(texta)
            dataa = (texta)
            print(dataa)

            db = pymysql.connect(host='localhost', user='root', passwd='Shubhh@95298', db='Air_Reservation',
                                     autocommit=True)

            cursor = db.cursor()

            '''Mysql for user input'''

            cursor.execute("DELETE FROM Flight WHERE flightId=%s", dataa)
            cursor.execute("SELECT * FROM Flight;")
            print(cursor.fetchall())

            db.close()

        Buttonh = Button(deleteFli, text="Save", command=delete).place(x=20, y=150)

    Button(master, text="Save", command=done).place(x=20, y=280)
    Button(master, text="Delete Flight", command=deleteFlight).place(x=20, y=310)
    flightId.grid(row=0, column=1)
    flightTerm.grid(row=1, column=1)
    flightTicket.grid(row=2, column=1)
    numFlights.grid(row=3, column=1)










def plane():

    master = Tk()
    master.geometry("1000x500")
    master.title("Air Reservation System")

    textArrival = StringVar()
    textDeparture = StringVar()
    textPlaneNum = StringVar()
    textSeatNum = StringVar()
    textPlaneSize = StringVar()

    Label(master, text="Arrival: ").grid(row=0)
    Label(master, text="Departure: ").grid(row=1)
    Label(master, text="Plane Number: ").grid(row=2)
    Label(master, text="Number of Seats: ").grid(row=3)
    Label(master, text="Plane Size: ").grid(row=4)

    Label(master, text="(Example of Arrival Time: HH:MM:SS (Insert time based on 24 hour clock)) ").grid(row=15)
    Label(master, text="(Example of Departure Time: HH:MM:SS (Insert time based on 24 hour clock)) ").grid(row=16)
    Label(master, text="(Example of Plane Number: 125588) ").grid(row=17)
    Label(master, text="(Example of Number of Seats: 100) ").grid(row=18)
    Label(master, text="(Example of Plane Size: Small,Medium, or Large) ").grid(row=19)
    Label(master, text="For reference on Plane Size, Small(150 feet long), Medium(200 feet long), Large(250 feet long)").grid(row=20)



    arrival = Entry(master, textvariable=textArrival)
    departure = Entry(master, textvariable=textDeparture)
    planeNum = Entry(master, textvariable=textPlaneNum)
    seatNum = Entry(master, textvariable = textSeatNum)
    planeSize = Entry(master, textvariable = textPlaneSize)

    def done():
        texta = "{}".format(arrival.get())
        textb = "{}".format(departure.get())
        textc = "{}".format(planeNum.get())
        textd = "{}".format(seatNum.get())
        texte = "{}".format(planeSize.get())
        print(texta)

        dataa = (texta, textb, textc, textd, texte)
        print(dataa)
        db = pymysql.connect(host='localhost', user='root', password='Shubhh@95298', database='Air_Reservation',
                             autocommit=True)
        cursor = db.cursor()
        '''Mysql for user input'''

        cursor.execute("INSERT INTO Plane VALUES (%s, %s, %s, %s, %s)", dataa)
        db.commit()

        cursor.execute("SELECT * FROM Plane;")
        print(cursor.fetchall())

        db.close()

    arrival.grid(row=0, column=1)
    departure.grid(row=1, column=1)
    Button(master, text="Save", command=done).place(x=20, y=270)
    planeNum.grid(row=2, column=1)
    seatNum.grid(row=3, column=1)
    planeSize.grid(row=4, column=1)



label = Label(root, text="WELCOME TO THE AIR RESERVATION SYSTEM", height=3, width=60, bg="lightblue")
label.place(relx=0.5, rely=0.12, anchor='n')

# Center frame to hold the main command buttons (auto centered)
center_frame = Frame(root, bg=None)
center_frame.place(relx=0.5, rely=0.5, anchor='center')

myButtonb = Button(center_frame, height=3, width=12, text="PLANE", command=plane, bg="lightpink")
myButtonc = Button(center_frame, height=3, width=12, text="TICKETS", command=ticket, bg="lightpink")
myButtond = Button(center_frame, height=3, width=12, text="FLIGHTS", command=flight, bg="lightpink")
myButtone = Button(center_frame, height=3, width=12, text="PASSENGER", command=passenger, bg="lightpink")

myButtonb.grid(row=0, column=0, pady=8)
myButtonc.grid(row=1, column=0, pady=8)
myButtond.grid(row=2, column=0, pady=8)
myButtone.grid(row=3, column=0, pady=8)




root.mainloop()