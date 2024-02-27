# LIM ZHI SHEN
# TP069606
# -----------------------------------------------Auxiliary function start-----------------------------------------------
def Count(a):  # build a list According list
    count1 = 0
    countlist = []
    for i in a:
        countlist.append(count1)
        count1 = count1 + 1
    return countlist


def Date(date):  # Validation +for date
    date1 = date.split("/")
    a, b = 0, 0
    if 0 > int(date1[2]) or int(date1[2]) >= 9999:
        raise ValueError
    if int(date1[2]) % 100 == 0:
        if int(date1[2]) % 400 == 0:
            a = 1
    else:
        a = 2
    if 1 <= int(date1[1]) <= 7:
        if int(date1[1]) % 2 == 0:
            b = 30
        else:
            b = 31
    elif 8 <= int(date1[1]) <= 12:
        if int(date1[1]) % 2 == 0:
            b = 31
        else:
            b = 30
    if int(date1[1]) == 2 and int(a) == 1:
        b = 29
    elif int(date1[1]) == 2 and int(a) == 2:
        b = 28
    if 0 >= int(date1[0]) or int(date1[0]) > int(b):
        raise ValueError
    return date


def Oneview(i):  # View a Groceries
    file = open("Groceries.txt", "r+")
    c = file.readlines()
    file.close()
    name = c[i].rstrip().split(";")[0]
    exp = c[i].rstrip().split(";")[1]
    price = c[i].rstrip().split(";")[2]
    sp = c[i].rstrip().split(";")[3]
    print("-" * 10, +int(i + 1), " item" + "-" * 10)
    print("Name:\t\t\t" + name + "\nExp Date:\t\t" + exp + "\nPrice:\t\t\t" + price + "\nSpecification:\t" + sp)


def exit():  # To Select exit or not
    print("-" * 34 + " Are you sure to exit" + "-" * 50)
    while True:
        try:
            a = input("Please enter your selection '1/yes or 2/no':")
            if a == "yes" or a == "1":
                return "1"
            elif a == "no" or a == "2":
                return "2"
            raise ValueError
        except:
            print("-" * 34 + " Please enter 1/yes or 2/no" + "-" * 50)


def WhoAreYou(customer):  # Check the number of customer from name
    with open("customer.txt", "r+") as file:
        c = file.readlines()
    for i in Count(c):
        if customer == c[i].rstrip().split(";")[0]:
            return (i)


def confirm():  # ReConfirm enter
    while True:
        try:
            enter = input("Are you sure to place order yes/no:")
            if enter == "yes":
                return True
            elif enter == "no":
                return False
        except:
            print("only can enter yes or no")


def ViewPersonal(customer):  # View Personal detail
    with open("customer.txt", 'r+') as file:
        c = file.readlines()
    print("-" * 10 + "Personal detail" + "-" * 18)
    for i in Count(c):
        if customer == c[i].rstrip().split(";")[0]:
            phone = c[i].rstrip().split(";")[4]
            email = c[i].rstrip().split(";")[5]
            gender = c[i].rstrip().split(";")[6]
            date = c[i].rstrip().split(";")[7]
            adds = c[i].rstrip().split(";")[8]
            print("Name:\t\t\t\t" + customer + "\nContact Number:\t\t" + str(phone) + "\nEmail:\t\t\t\t"
                  + email + '\nGender:\t\t\t\t' + gender + "\nDate of Birth:\t\t" + date + "\nAddress:\t\t\t" + adds)
    dsa = input("-" * 10 + "Press enter to exit" + "-" * 18)


def twoplace(a):  # only two decimal places
    c = str(a).split(".")[0]
    d = str(a).split(".")[1][:2]
    e = str(a).split(".")[1][2:4]
    if e == "99":
        f = int(d) + 1
        b = c + "." + str(f)
    else:
        b = c + "." + d
    return b


# -----------------------------------------------Auxiliary function end-------------------------------------------------
# -----------------------------------------------Login function start-------------------------------------------------

def login():  # Login
    print("-" * 34 + " FRESHCO Sdn Bhd" + "-" * 50)
    print("Welcome to login page")
    while True:
        try:
            user = input("Please enter your userid:")
            if user == "exit":
                return ("exit",0)
            userpass = input("Please enter your password:")
            if userpass == "exit":
                return ("exit",0)
            file = open("customer.txt", "r+")
            file.seek(0)
            lines = file.readlines()
            file.close()
            numberlist = Count(lines)
            for i in numberlist:
                userid = lines[i].rstrip().split(";")[1]
                password = lines[i].rstrip().split(";")[2]
                if user == userid and password == userpass:
                    if int(i) == 0:
                        return ("admin", i)
                    else:
                        return ("customer", i)
            raise ValueError
        except:
            print("Login Userid or Password is wrong, to exit Login page enter 'exit'")


# -----------------------------------------------Login function end----------------------------------------------------
# -----------------------------------------------All register function start--------------------------------------------
def register():  # register a new customer
    print("-" * 34 + " FRESHCO Sdn Bhd" + "-" * 50)
    print("Welcome to registration page")
    while True:
        try:
            name = input("Please enter your name:")
            if name == "exit":
                break
            email = emailformat()
            if email == "exit":
                break
            contact = phonenumber()
            if contact == "exit":
                break
            gender = Gender()
            if gender == "exit":
                break
            date = DateofBirth()
            if date == "exit":
                break
            address = input("Please enter your address:")
            userid = input("Please enter your userid:")
            password = Password()
            if password == "exit":
                break
            file = open("customer.txt", "a+")
            file.seek(0)
            file.write(
                name + ";" + userid + ";" + password + ";0;" + contact + ";" + email + ";" + gender
                + ";" + date + ";" + address + ";\n")
            file.close()
            print("-" * 100)
            print("register sucess")
            print("Thank for your registration")
            dsa = input("-" * 10 + "Press enter to exit" + "-" * 18)
            break
        except:
            print("system break dowwn")


def emailformat():  # email input and detection is correct
    while True:
        try:
            email = input("Please enter your email:")
            if email == "exit":
                return "exit"
            a = email.split('@')[1]
            a_type = a.split('.')[1]
            if a_type == "com":
                return email
        except:
            print("-" * 100)
            print("This is not email format!\n\tTo exit register enter 'exit'")


def phonenumber():  # Phone number input and detection is correct
    while True:
        try:
            count = 0
            phone = input("Please enter malaysia contact number from'01':")
            if phone == "exit":
                return "exit"
            for i in phone:
                count = count + 1
            if count != 10:
                raise ValueError
            if phone[:2] != "01":
                raise ValueError
            return phone
        except:
            print("-" * 100)
            print("This is not Malaysia phone format!\n\tTo exit register enter 'exit'")


def Gender():  # Gender input and detection is correct
    while True:
        try:
            x = ["Male", "Female", "Other"]
            gender = input("Please enter your gender('Male,Female,Other):")
            if gender == "exit":
                return "exit"
            for i in x:
                if gender == i:
                    return gender
            raise ValueError
        except:
            print("-" * 100)
            print("Please enter Male/Female/Other only!\n\tTo exit register enter 'exit'")


def DateofBirth():  # Date input and detection is correct
    while True:
        try:
            date = input("Please enter Date of Birth by DD/MM/YYYY:")
            if date == "exit":
                return "exit"
            Date(date)
            return date
        except:
            print("-" * 100)
            print("Enter by DD/MM/YYYY!\n\tTo exit register enter 'exit'")


def Password():  # Password input and detection is correct
    while True:
        try:
            password = input("Please enter your password:")
            if password == "exit":
                return "exit"
            repassword = input("Please reenter your password:")
            if password != repassword:
                raise ValueError
            return password
        except:
            print("-" * 100)
            print("Duplicate password is wrong!\n\tTo exit register enter 'exit'")


# -----------------------------------------------All register function end---------------------------------------------

# -----------------------------------------------Add Groceries start----------------------------------------------------
def AddGroceries():  # Add Groceries and make sure is in correct
    while True:
        try:
            print("-" * 34 + " AddGroceries page FRESHCO Sdn Bhd" + "-" * 35)
            name = Name()
            if name == 'exit':
                break
            exp = Exp()
            if exp == 'exit':
                break
            price = float(input("Please input Groceries price:"))
            if price<=0 or price>9999:
                raise ValueError
            price = twoplace(price)
            specification = Specificationgroceries()
            if specification == "exit":
                break
            file = open("Groceries.txt", "a+")
            file.write(name + ";" + exp + ";" + str(price) + ";" + specification + "\n")
            file.close()
            print("Successful Add new Groceries ")
            dsa = input("-" * 10 + "Press enter to exit" + "-" * 18)
            break
        except:
            print("Something Wrong\nTo exit Add Groceries enter 'exit'")


def Name():  # Name input and detection is no reply
    file = open("Groceries.txt", "r+")
    c = file.readlines()
    file.close()
    while True:
        try:
            name = input("Please input Groceries name:")
            if name == "exit":
                return "exit"
            for i in Count(c):
                gro = c[i].rstrip().split(";")[0]
                if gro == name:
                    raise ValueError
            return name
        except:
            print("-" * 34 + " Name FRESHCO Sdn Bhd" + "-" * 35)
            print("The same grocery name already exists\nTo exit Add Groceries enter 'exit' ")


def Exp():  # For input exp and use Date function
    while True:
        try:
            exp = input("Please input Groceries exp date:")
            if exp == "exit":
                return "exit"
            Date(exp)
            return exp
        except:
            print("-" * 34 + " Exp Date FRESHCO Sdn Bhd" + "-" * 35)
            print("Enter by DD/MM/YYYY!\n\tTo exit Add Groceries enter 'exit'")


def Specificationgroceries():  # SPecification input and detection is correct
    a = ["Piece", "Perkg", "Pack", "etc"]
    while True:
        try:
            sp = input("Piece\tPerkg\tPack\tetc\nPlease input specification:")
            if sp == "exit":
                return "exit"
            for i in a:
                if sp == i:
                    return sp
            raise ValueError
        except:
            print("-" * 34 + " Specification FRESHCO Sdn Bhd" + "-" * 35)
            print("Only can input Piece\tPerkg\tPack\tetc\nTo exit Add Groceries enter 'exit'")


# -----------------------------------------------Add Groceries end------------------------------------------------------
# -----------------------------------------------Groceries function start-----------------------------------------
def ViewGroceries():  # View all Groceries
    file = open("Groceries.txt", "r+")
    c = file.readlines()
    file.close()
    for i in Count(c):
        name = c[i].rstrip().split(";")[0]
        exp = c[i].rstrip().split(";")[1]
        price = c[i].rstrip().split(";")[2]
        sp = c[i].rstrip().split(";")[3]
        print("-" * 10, +int(i + 1), " item" + "-" * 10)
        print("Name:\t\t\t" + name + "\nExp Date:\t\t" + exp + "\nPrice:\t\t\t" + price + "\nSpecification:\t" + sp)
    print("-" * 10 + "All item have been list" + "-" * 10)
    dsa = input("-" * 10 + "Press enter to exit" + "-" * 18)


def UpdateGroceries():  # UpdateGroceries and detection is correct
    print("-" * 34 + " Update Groceries FRESHCO Sdn Bhd" + "-" * 35)
    file = open("Groceries.txt", "r+")
    c = file.readlines()
    file.close()
    while True:
        try:
            stop = 0
            for i in Count(c):
                print(i + 1, c[i].strip().split(";")[0])
            a = (input("Which item you want to Modify:"))
            if a == "exit":
                break
            for i in Count(c):
                if int(int(a) - 1) == int(i):
                    Oneview(i)
                    name = c[i].rstrip().rsplit(";")[0]
                    exp = Exp()
                    if exp == 'exit':
                        break
                    price = float(input("Please input Groceries price:"))
                    if 0<=price<=99999:
                        price = twoplace(price)
                        specification = Specificationgroceries()
                        if specification == "exit":
                            break
                        new = (name + ";" + exp + ";" + str(price) + ";" + specification + "\n")
                        print(new)
                        replacement = ""
                        for line in Count(c):
                            if i == line:
                                replacement = replacement + (new) + ""
                            else:
                                replacement = replacement + (c[line]) + ""
                        file = open("Groceries.txt", "w+")
                        file.seek(0)
                        file.write(replacement)
                        file.close()
                        print("Successful Update Groceries")
                        stop = 1
                        break
            if stop == 1:
                dsa = input("-" * 10 + "Press enter to exit" + "-" * 18)
                break
            raise ValueError
        except:
            print("-" * 34 + " Update Groceries FRESHCO Sdn Bhd" + "-" * 35)
            print("Something get wrong\nTo exit Update Groceries enter 'exit'")


def DeleteGroceries():  # Delete Groceries
    while True:
        file = open("Groceries.txt", "r+")
        c = file.readlines()
        file.close()
        for i in Count(c):
            name = c[i].rstrip().split(";")[0]
            print(i + 1, "  " + name)
        stop = False
        print("-" * 34 + " Delete Groceries Page FRESHCO Sdn Bhd" + "-" * 35)
        try:
            delete = input("Which item did you want to Delete(number):")
            if delete == "exit":
                break
            clean = input("Are you sure to delete enter 'yes' or '1':")
            if clean == "yes" or clean == "1":
                for i in Count(c):
                    if int(i) == (int(delete) - 1):
                        replacement = ""
                        for line in Count(c):
                            if (int(delete) - 1) == line:
                                print("Successful to Delete Groceries")
                            else:
                                replacement = replacement + (c[line]) + ""
                        file = open("Groceries.txt", "w+")
                        file.seek(0)
                        file.write(replacement)
                        file.close()
                        stop = True
            if stop == True:
                dsa = input("-" * 10 + "Press enter to exit" + "-" * 18)
                break
            else:
                print("Fail to delete Groceries")
                dsa = input("-" * 10 + "Press enter to continue" + "-" * 18)
        except:
            print("-" * 34 + " Delete Groceries Page FRESHCO Sdn Bhd" + "-" * 35)
            print("Please enter in number\nTo exit Delete Groceries Page enter 'exit'")


# -----------------------------------------------Groceries function end-----------------------------------------------
# -----------------------------------------------Order function start-------------------------------------------------
def Viewallorder():  # View all order
    print("-" * 34 + " View all order FRESHCO Sdn Bhd" + "-" * 35)
    file = open("order.txt", "r+")
    c = file.readlines()
    file.close()
    for i in Count(c):
        name = c[i].rstrip().split(";")[0]
        amount = c[i].rstrip().split(";")[1]
        groceries = c[i].rstrip().split(";")[2]
        amoutprice = c[i].rstrip().split(";")[3]
        price = c[i].rstrip().split(";")[4]
        sp = c[i].rstrip().split(";")[5]
        phone = c[i].rstrip().split(";")[6]
        address = c[i].rstrip().split(";")[7]
        print("-" * 10, +int(i + 1), " order" + "-" * 10)
        print("Name:\t\t\t" + name + "\nAmount:\t\t\t" + amount + "\nGroceries name:\t" + groceries +
              "\nPayment\t\t\t" + amoutprice + "\nUnit Price:\t\t" + price +
              "\nSpecification:\t" + sp + "\nPhone number:\t" + phone + "\nAddress:\t\t" + address)
    print("-" * 10 + "All order have been list" + "-" * 10)
    dsa = input("-" * 10 + "Press enter to exit" + "-" * 18)


def Placeorder(customer):  # Place order page
    print("-" * 34 + " Place order FRESHCO Sdn Bhd" + "-" * 35)
    file = open("Groceries.txt", "r+")
    c = file.readlines()
    file.close()
    while True:
        try:
            file = open("customer.txt", "r+")
            d = file.readlines()
            file.close()
            k = 1
            stop = False
            success = False
            print("-" * 10 + customer + ", Welcome to order page" + "-" * 8)
            for i in Count(c):
                print("%s %+15s   Price:%+10s"
                      % ((int(int(i) + 1)), (c[i].rstrip().split(";")[0]), (c[i].rstrip().split(";")[2])))
                k = k + 1
            choose = input("Please enter the number of the item you want to buy:")
            if choose == "exit":
                break
            if 0 > int(choose) or int(choose) >= k:
                raise ValueError
            amount = int(input("Please enter the quantity you want to buy:"))
            if 0>=amount or amount>=9999:
                raise ValueError
            for i in Count(c):
                if (int(choose) - 1) == i:
                    gname = c[i].rstrip().split(";")[0]
                    gprice = c[i].rstrip().split(";")[2]
                    specifi = c[i].rstrip().split(";")[3]
                    for j in Count(d):
                        if str(customer) == str(d[j].rstrip().split(";")[0]):
                            balance = d[j].rstrip().split(";")[3]
                            payment = float(gprice) * float(amount)
                            payment = twoplace(payment)
                            print("-" * 10 + "Confirm details" + "-" * 18)
                            print("Name:\t\t" + customer + "\nBuy Amount:\t" + str(amount) + "\nItem:\t\t" + gname +
                                  "\nPayment:\t" + str(payment) + "\nWallet Amount:\t" + str(balance))
                            print("-" * 10 + "Confirm details" + "-" * 18)
                            print("Your Wallet balance is:\t", balance)
                            print("Need to pay:\t\t\t", payment)
                            con = confirm()
                            if con == True and float(balance) < float(payment):
                                print("-" * 10 + "Insufficient balance in wallet to pay" + "-" * 8)
                                topup = input("Do you want to Topup, if need type 'yes':")
                                if topup == "yes":
                                    balance = Topup(customer)
                                    print("-" * 10 + "Confirm details" + "-" * 18)
                                    print("Name:\t\t" + customer + "\nBuy Amount:\t" + str(amount) + "\nItem:\t\t"
                                          + gname + "\nPayment:\t" + str(payment) + "\nWallet Amount:\t" + str(balance))
                                    print("-" * 10 + "Confirm details" + "-" * 18)
                                    print("Your Wallet balance is:\t", balance)
                                    print("Need to pay:\t\t\t", payment)
                                    con = confirm()

                            if con == True:
                                if float(balance) < float(payment):
                                    print("No enough of balance")
                                    print("The order was unsuccessful")
                                    dsa = input("-" * 10 + "Press enter to continue" + "-" * 18)
                                    stop = True
                                elif float(payment) <= float(balance):
                                    replacement = ""
                                    for line in Count(d):
                                        if (customer) == d[line].rstrip().rsplit(";")[0]:
                                            name = d[line].rstrip().rsplit(";")[0]
                                            userid = d[line].rstrip().rsplit(";")[1]
                                            password = d[line].rstrip().rsplit(";")[2]
                                            newa = float(balance) - float(payment)
                                            contact = d[line].rstrip().rsplit(";")[4]
                                            email = d[line].rstrip().rsplit(";")[5]
                                            gender = d[line].rstrip().rsplit(";")[6]
                                            date = d[line].rstrip().rsplit(";")[7]
                                            addss = d[line].rstrip().rsplit(";")[8]
                                            newb = twoplace(newa)
                                            new = (name + ";" + userid + ";" + password + ";" + str(newb) + ";" +
                                                   contact + ";" + email + ";" + gender + ";" + date + ";" + addss +
                                                   ";\n")
                                            order = (customer + ";" + str(amount) + ";" + gname + ";" + str(
                                                payment) + ";" + str(
                                                gprice) + ";" + specifi + ";" + str(contact) + ";" + addss + ";\n")
                                            file = open("order.txt", "a+")
                                            file.write(order)
                                            file.close()
                                            replacement = replacement + new + ""
                                            stop = True
                                            success = True
                                        else:
                                            replacement = replacement + (d[line]) + ""
                                    file = open("customer.txt", "w")
                                    file.seek(0)
                                    file.write(replacement)
                                    file.close()
                                    print("-" * 10 + "Succesful to place order" + "-" * 18)
                                    dsa = input("-" * 10 + "Press enter to exit" + "-" * 18)
                            elif con == False:
                                print("The order was unsuccessful")
                                dsa = input("-" * 10 + "Press enter to continue" + "-" * 18)
                        if stop == True:
                            break
                if stop == True:
                    break
            if success == True:
                break


        except:
            print("To exit type'exit'")


def ViewownOrder(customer):  # Customer view their own order
    with open("order.txt", "r+") as file:
        c = file.readlines()
    a = 0
    for i in Count(c):
        if customer == c[i].rstrip().split(";")[0]:
            a = a + 1
            name = c[i].rstrip().split(";")[0]
            amount = c[i].rstrip().split(";")[1]
            groceries = c[i].rstrip().split(";")[2]
            amoutprice = c[i].rstrip().split(";")[3]
            price = c[i].rstrip().split(";")[4]
            sp = c[i].rstrip().split(";")[5]
            phone = c[i].rstrip().split(";")[6]
            address = c[i].rstrip().split(";")[7]
            print("-" * 10, +int(a), " order" + "-" * 10)
            print("Name:\t\t\t" + name + "\nAmount:\t\t\t" + amount + "\nGroceries name:\t" + groceries +
                  "\nPayment\t\t\t" + amoutprice + "\nUnit Price:\t\t" + price +
                  "\nSpecification:\t" + sp + "\nPhone number:\t" + phone + "\nAddress:\t\t" + address)
    if a >= 1:
        print("-" * 10 + "Your order have been list" + "-" * 10)
    else:
        print("-" * 10 + "No Have any order" + "-" * 10)
    abc = input("-" * 10 + "Press enter to exit" + "-" * 18)


# -----------------------------------------------Order function end-----------------------------------------------------
# -----------------------------------------------Wallet function end---------------------------------------------------
def Topup(customer):  # Customer Top Up their wallet
    print("-" * 34 + " Top Up Wallet FRESHCO Sdn Bhd" + "-" * 35)
    file = open("customer.txt", "r+")
    c = file.readlines()
    file.close()
    a = WhoAreYou(customer)
    while True:
        try:
            print("Your wallet balance is:", c[a].rstrip().rsplit(";")[3])
            value = input("How much do you want to topup:")
            if value == "exit":
                break
            if 0 <= int(value) <= 9999999:
                user = input("Please enter your userid:\t")
                password = input("Please enter your password:\t")
                if user == c[a].rstrip().split(";")[1] and password == c[a].rstrip().split(";")[2]:
                    replacement = ""
                    for line in Count(c):
                        if (customer) == c[line].rstrip().rsplit(";")[0]:
                            name = c[line].rstrip().rsplit(";")[0]
                            userid = c[line].rstrip().rsplit(";")[1]
                            password = c[line].rstrip().rsplit(";")[2]
                            newa = float(c[line].rstrip().split(";")[3]) + float(value)
                            contact = c[line].rstrip().rsplit(";")[4]
                            email = c[line].rstrip().rsplit(";")[5]
                            gender = c[line].rstrip().rsplit(";")[6]
                            date = c[line].rstrip().rsplit(";")[7]
                            addss = c[line].rstrip().rsplit(";")[8]
                            newb = twoplace(newa)
                            new = (name + ";" + userid + ";" + password + ";" + str(newb) + ";" + contact +
                                   ";" + email + ";" + gender + ";" + date + ";" + addss + ";\n")
                            replacement = replacement + new + ""
                        else:
                            replacement = replacement + (c[line]) + ""
                    file = open("customer.txt", "w+")
                    file.seek(0)
                    file.write(replacement)
                    file.close()
                    with open("customer.txt", "r+") as file:
                        d = file.readlines()
                    newbalan = (d[a].rstrip().rsplit(";")[3])
                    print("-" * 10 + "Succesful to Topup" + "-" * 18)
                    print("Your wallet balance is:", newbalan)
                    dsa = input("-" * 10 + "Press enter to exit" + "-" * 18)
                    return (str(newbalan))
                else:
                    print("-" * 10 + " Userid or Password is wrong" + "-" * 18)
            else:
                raise ValueError
        except:
            print("Something wrong")
            print("To exit type'exit'")
            print("-" * 10 + " Topup" + "-" * 18)


def ViewWallet(customer):  # Customer View their wallet
    print("-" * 10 + "Wallet Balance" + "-" * 18)
    with open("customer.txt", "r+") as file:
        c = file.readlines()
    num = WhoAreYou(customer)
    print("Your wallet balance is:", c[num].rstrip().rsplit(";")[3])
    dsa = input("-" * 10 + "Press enter to exit" + "-" * 18)


# -----------------------------------------------Search function start------------------------------------------------
def Searchforspecific():  # Search with speccific and show Groceries
    a = ["Piece", "Perkg", "Pack", "etc"]
    print("-" * 34 + " Search for Specification FRESHCO Sdn Bhd" + "-" * 35)
    while True:
        try:
            stop = False
            sp = input("Piece\tPerkg\tPack\tetc\nPlease input specification:")
            if sp == "exit":
                return "exit"
            file = open("Groceries.txt", "r+")
            c = file.readlines()
            file.close()
            for i in Count(c):
                if sp == (c[i].strip().split(";")[3]):
                    Oneview(i)
                    stop = True
            if stop:
                dsa = input("-" * 10 + "Press enter to exit" + "-" * 18)
                break
            raise ValueError
        except:
            print("-" * 34 + " Search for Specification FRESHCO Sdn Bhd" + "-" * 35)
            print("Only can input Piece\tPerkg\tPack\tetc\nTo exit Search for Specification enter 'exit'")


def Searchorderofcustomer():  # Search with specific order and show customer
    print("-" * 34 + " Search order of Customer FRESHCO Sdn Bhd" + "-" * 35)
    file = open("Groceries.txt", "r+")
    c = file.readlines()
    file.close()
    file = open("order.txt", "r+")
    d = file.readlines()
    file.close()
    for i in Count(c):
        name = c[i].rstrip().split(";")[0]
        print(i + 1, "  " + name)
    while True:
        try:
            emptystop = False
            stop = False
            search = input("Which order did you want to search:")
            if search == 'exit':
                break
            for j in Count(c):
                if (int(search) - 1) == int(j):
                    emptystop = True
                    for i in Count(d):
                        if c[j].rstrip().split(";")[0] == d[i].rstrip().split(";")[2]:
                            stop = True
                            name = d[i].rstrip().split(";")[0]
                            amount = d[i].rstrip().split(";")[1]
                            groceries = d[i].rstrip().split(";")[2]
                            amoutprice = d[i].rstrip().split(";")[3]
                            price = d[i].rstrip().split(";")[4]
                            print("-" * 10, " order" + "-" * 10)
                            print("Name:\t\t\t" + name + "\nAmount:\t\t\t" + amount + "\nGroceries name:\t"
                                  + groceries + "\nPayment:\t\t" + amoutprice + "\nUnit Price:\t\t" + price)
            if emptystop == True:
                print("-" * 10, c[int(search) - 1].rstrip().split(";")[0] + " without any order" + "-" * 10)
                break
            elif stop == True:
                print("-" * 10, "All order have been presented" + " order" + "-" * 10)
                dsa = input("-" * 10 + "Press enter to exit" + "-" * 18)
                break
            else:
                raise ValueError
        except:
            print("-" * 34 + " Search order of Customer FRESHCO Sdn Bhd" + "-" * 35)
            print("Please enter in number\nTo exit Search order of Customer enter 'exit'")


def Searchcustomerfororder():
    print("-" * 34 + " Search customer order FRESHCO Sdn Bhd" + "-" * 35)
    with open("customer.txt", "r+") as file:
        c = file.readlines()
    while True:
        for i in Count(c):
            if i != 0:
                print("%d. %s" % (i, (c[i].rstrip().rsplit(";")[0])))
        choose = input("Please input number of customer you want to search:")
        for i in Count(c):
            if int(choose) == i:
                name = c[i].rstrip().rsplit(";")[0]
                ViewownOrder(name)
                return
        print("-" * 10 + "Wrong Input" + "-" * 10)


# -----------------------------------------------Search function end------------------------------------------------
# -----------------------------------------------Main script start--------------------------------------------------
while True:
    stop = False
    print("-" * 100)
    print("Welcome to the 'FRESHCO Sdn Bhd' Groceries:\n\t1.Login\n\t2.Register\n\t3.New Customer\n\t4.Exit")
    choose = input("Your Selecetion is (number):")
    if choose == "1":
        user = login()
        if user[0]=="exit":
            continue
        if user[0] == "admin":
            file = open("customer.txt", "r+")
            save = file.readlines()
            file.close()
            name = save[user[1]].rstrip().split(";")[0]
            while True:
                try:
                    print("-" * 34 + " Admin page FRESHCO Sdn Bhd" + "-" * 35)
                    print(
                        "Admin " + name + ", welcome Please choose from the options below :\n\t1.ADD new Groceries\n\t"
                                          "2.View all Groceries detail\n\t3.Update/modify Groceries information\n\t"
                                          "4.Search some grocery details by using their specification\n\t"
                                          "5.View all order\n\t"
                                          "6.view which customers have placed an order for these certain groceries\n\t"
                                          "7.Delete Groceries\n\t8.Search order history of certain customer\n\t9.Exit")
                    choose = int(input("Please enter your Selection:"))
                    if choose == 1:
                        AddGroceries()
                    elif choose == 2:
                        ViewGroceries()
                    elif choose == 3:
                        UpdateGroceries()
                    elif choose == 4:
                        Searchforspecific()
                    elif choose == 5:
                        Viewallorder()
                    elif choose == 6:
                        Searchorderofcustomer()
                    elif choose == 7:
                        DeleteGroceries()
                    elif choose == 8:
                        Searchcustomerfororder()
                    elif choose == 9:
                        a = exit()
                        if int(a) == 1:
                            print("-" * 34 + "Which page do you want to exit to " + "-" * 50)
                            print("\t\t\t1.Mainpage\n\t\t\t2.Exit Groceries")
                            a = input("Please enter your selection:")
                            if a == "1":
                                break
                            elif a == "2":
                                stop = True
                                break
                            else:
                                print("-" * 34 + " Exit Fail" + "-" * 35)
                        elif int(a) == 2:
                            print("-" * 34 + " No Exit" + "-" * 50)
                except:
                    print("-" * 34 + " Admin page FRESHCO Sdn Bhd" + "-" * 35)
                    print("Please enter 1-8 in number")
            if stop:
                break
        elif user[0] == "customer":
            while True:
                file = open("customer.txt", "r+")
                save = file.readlines()
                file.close()
                customer = save[user[1]].rstrip().split(";")[0]
                try:
                    print("-" * 34 + " FRESHCO Sdn Bhd" + "-" * 50)
                    print(
                        str(customer) + ", welcome Please choose from the options below :\n\t"
                                        "1.View all Groceries detail\n\t"
                                        "2.Place order\n\t3.View Wallet Balance\n\t4.Top up Wallet\n\t"
                                        "5.View own order\n\t6.View personal information\n\t7.Exit")
                    choose = int(input("Please enter your Selectionin number:"))
                    if choose == 1:
                        ViewGroceries()
                    elif choose == 2:
                        Placeorder(customer)
                    elif choose == 3:
                        ViewWallet(customer)
                    elif choose == 4:
                        Topup(customer)
                    elif choose == 5:
                        ViewownOrder(customer)
                    elif choose == 6:
                        ViewPersonal(customer)
                    elif choose == 7:
                        ab = exit()
                        if int(ab) == 1:
                            print("-" * 34 + "Which page do you want to exit to " + "-" * 50)
                            print("\t\t\t1.Mainpage\n\t\t\t2.Exit Groceries")
                            a = input("Please enter your selection:")
                            if a == "1":
                                break
                            elif a == "2":
                                stop = True
                                break
                            else:
                                print("-" * 34 + " Exit Fail" + "-" * 35)
                        elif int(ab) == 2:
                            print("-" * 34 + " No Exit" + "-" * 50)
                except:
                    print("-" * 34 + " Customer page FRESHCO Sdn Bhd" + "-" * 35)
                    print("Please enter 1-7 in number")
            if stop:
                break
    elif choose == "2":
        register()
    elif choose == "3":
        while True:
            print("-" * 34 + " New Customer FRESHCO Sdn Bhd" + "-" * 35)
            print(
                "Welcome to the 'FRESHCO Sdn Bhd' Groceries:\n\t1.View all Groceries detail\n\t2.Register\n\t3.Exit")
            choose = input("Your Selecetion is (number):")
            if choose == "1":
                ViewGroceries()
            elif choose == "2":
                register()
                break
            elif choose == "3":
                break
            else:
                print("-" * 34 + " Wrong Input" + "-" * 50)
    elif choose == "4":
        break
    else:
        print("-" * 34 + " Wrong input" + "-" * 50)
# -----------------------------------------------Main function end--------------------------------------------------
