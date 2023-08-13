# Pizza Shop
# --------------- Imported Modules ------------------
from datetime import datetime
import uuid, shutil, re
from database import save_data_into_db

# --------------- Global Variables-------------------
terminal_size = shutil.get_terminal_size().columns
now = datetime.now()
regex = re.compile("[@_!#$%^&*()<>?/\\|}{~:',.;`₹]")


# Rastaurent Menu in the form of Dictionary.
ITEMS = {'Veg-Items': {101 : {'Magherita': 219},
            102 : {'Double Cheese Magherita': 319},
            103 : {'Farm House': 199},
            104 : {'Peppy Paneer': 119},
            105 : {'Mexican Green Wave': 399},
            106 : {'Deluxe Veggie': 199},
            107 : {'Veg Extravaganza': 319},
            108 : {'Cheese N Corn': 199},
            109 : {'Paneer Makhani': 259},
            110 : {'Veggie Paradise': 269},
            111 : {'Fresh Veggie': 219},
            112 : {'Indi Tandoori Paneer': 459}},
       'Non-Veg-Items': {201 : {'Chicken Sausage': 305},
                202 : {'Pepper Barbecue Chicken': 335},
                203 : {'Pepper Barbecue & Onion': 395},
                204 : {'Peri Peri Chicken': 395},
                205 : {'Chicken Golden Delight': 450},
                206 : {'Chicken Fiesta':450},
                207 : {'Chicken Dominator': 570},
                208 : {'Non Veg Supreme': 570},
                209 : {'Chicken Pepperoni': 589},
                210 : {'Indi Chicken Tikka': 589}},
       'Toppings': {301 : {'Pepperoni': 69},
            302 : {'Mushrooms': 59},
            303 : {'Onions': 39},
            304 : {'Sausage': 59},
            305 : {'Bacon': 49},
            306 : {'Extra Cheese': 89},
            307 : {'Black Olives': 49},
            308 : {'Green Peppers': 59},
            309 : {'Pineapple': 39},
            310 : {'Spinach': 39}},
       'Drinks': {401 : {'Coke': 69},
        402 : {'Pepsi': 59},
        403 : {'Sprite': 59},
        404 : {'Dew': 59},
        405 : {'Limca': 48},
        406 : {'Soda': 45},
        407 : {'Ice Tea': 49},
        408 : {'Ice Coffee': 66},
        409 : {'Mirinda': 48},
        410 : {'Thumbs Up': 69}}}


# There will be crder data store.
data = {}


def show_items():
    ''' This function printing Menu in Structure manner. '''

    # ------------- Shop Detail in Menu ----------------
    print("Noida's Pizza!!".center(terminal_size))
    print('Sector-**'.center(terminal_size))
    print('Noida, G.B Nagar, U.P'.center(terminal_size))
    print('------------------------------------------------'.center(terminal_size))
    print('Here is our menu:-\n'.center(terminal_size - 28))
    print('================================================'.center(terminal_size))

    # f = open('data.txt', 'a')
    f = None

    # All menu dictionary items will be printed from here.
    for item in ITEMS.items():
        print(f'{item[0]}:-'.center(terminal_size - 60), file = f)
        print('------------------------------------------------'.center(terminal_size), file = f)
        print('{:<10} {:<30} {}'.center(terminal_size - 30).format('CODE', 'ITEMS', 'PRICE'), file = f)
        print('------------------------------------------------'.center(terminal_size), file = f)
        # print(file = f)
        for code in item[1].items():
            for item_name, item_rate in code[1].items():
                print('{:<10} {:<30} {}'.center(terminal_size - 30).format(code[0], item_name, item_rate), file = f)
                print('------------------------------------------------'.center(terminal_size), file = f)
    # f.close()
                

    # Item choice will be entered here.
    break_point = True
    while break_point:
        ask = input("(To remove any item just put '-' before 'Sno.')\n(E.g- '-1')\n(Press Enter to cancel your order)\
            \nEnter the item's code or Enter '0' to Continue : ")
        if (ask == '0'):
            break_point = False
        elif (not ask):
            confirm = input('Are you sure to cancel your order? (y/n) :')
            if (not confirm):
                data.clear()
                show_items()
                break
            elif (confirm == 'n') or (confirm == 'N'):
                None
            elif (confirm == 'y') or (confirm == 'Y'):
                data.clear()
                show_items()
                break
        elif ('-' in ask):
            new_ask = ask.replace('-', '')
            data.pop(list(data)[int(new_ask) - 1])
            review_func('yes')
        elif ('*' in ask):
            try:
                item_code = int(ask.split('*')[0])
                item_qnty = int(ask.split('*')[1])
                for item in ITEMS.items():
                    try:
                        item_data = item[1][item_code]
                        valid_code = True
                        break
                    except:
                        valid_code = False
                if (valid_code == True):
                    data[item_code] = [item_data, item_qnty]
                    review_func('Yes')
                else:
                    print('\nPlease Enter code Properly!!')    
            except:
                print('\nPlease Enter code Properly!!')    
        elif (ask.isspace() == True):
            print('\nPlease Enter code Properly!!')
        elif (ask.isalpha() == True):
            print('\nPlease Enter code Properly!!')
        elif (regex.search(ask)):
            print('\nPlease Enter code Properly!!')
        else:
            ask = int(ask)
            qnty = 1
            for item in ITEMS.items():
                try:
                    item_data = item[1][ask]
                    valid_code = True
                    break
                except:
                    valid_code = False
            if valid_code == True:
                data[ask] = [item_data, qnty]
                review_func('Yes')
            else:
                print('\nPlease Enter code Properly!!')


def review_func(review):
    ''' This function will be used for review of customer order. '''

    # This function read order from data dictionary.
    if review.lower() == 'yes':

        # Printing review in Structured order. 
        print('\nYou ordered the followings items..\n'.center(terminal_size))
        print('{:<3} {:<25} {:<10} {:<10}'.format('SNO', 'ORDERED ITEMS', '', 'RATE').center(terminal_size + 6))
        print('================================================'.center(terminal_size))
        total_rate = 0      # To Calculate total rate.
        for i, item in enumerate(data.items()):
            for item_name, item_rate in item[1][0].items():
                print('{}.  {:<25} {:<10} {:<10}'.format(i+1, item_name, f'[x{item[1][1]}]', item[1][1]*item_rate).center(terminal_size + 6))
                total_rate += int(item[1][1]) * int(item_rate)
        print('================================================'.center(terminal_size))
        print('{}  {:<28} {:<5} {}'.format('  ', 'You have to pay - ', '', total_rate).center(terminal_size))
        print('------------------------------------------------'.center(terminal_size))


def bill_func(okay):
    ''' This function will be printing the bill of your order. '''

    
    if okay == '1':

        # Taking Customer name and phone no.
        print('\n----------------------------------------')
        cstmr_nm = str(input('Please Write Your name : '))
        if (cstmr_nm.isdigit() == True):
            print('\nPlease Enter your details Properly!')
            bill_func(okay)
        elif (not cstmr_nm):
            print('\nPlease Enter your details Properly!')
            bill_func(okay)

        cstmr_phn = str(input('Please Enter your Phone No. : '))
        if (cstmr_phn.isalpha() == True):
            print('\nPlease Enter your details Properly!')
            bill_func(okay)
        elif (not cstmr_nm):
            print('\nPlease Enter your details Properly!')
            bill_func(okay)
        elif (not len(cstmr_phn) == 10):
            print('\nPlease Enter your details Properly!')
            bill_func(okay)

        # Format of bill.
        print('----------------------------------------')
        print('**** Bill ****'.center(terminal_size))
        print("** Noida's Pizza **".center(terminal_size))
        print('Sector-**'.center(terminal_size))
        print('Noida, G.B Nagar, U.P'.center(terminal_size))
        print('------------------------------------------------'.center(terminal_size))
        print(now.strftime("%d/%m/%Y  %H:%M:%S").center(terminal_size))
        print(f"Order Id : {str(uuid.uuid4().fields[-1])[:14]}".center(terminal_size))
        print(f"Name : {cstmr_nm}".center(terminal_size))
        print(f"Phone no. : {cstmr_phn}".center(terminal_size))
        print('------------------------------------------------'.center(terminal_size))

        # Calculating total rate and printing final bill.
        total_rate = 0
        save_item = []
        print('{} {:<25} {:<10} {:<10}'.format('SNO', 'ORDERED ITEMS', '', 'RATE').center(terminal_size + 6))
        for i, item in enumerate(data.items()):
            for item_name, item_rate in item[1][0].items():
                print('{}.  {:<25} {:<10} {:<10}'.format(i+1, item_name, f'[x{item[1][1]}]', item[1][1]*item_rate).center(terminal_size + 6))
                total_rate += int(item[1][1]) * int(item_rate)
                save_item.append(item_name)
        print('================================================'.center(terminal_size))
        print('{}  {:<25} {:<10} {}'.format(' ', 'Total Rate - ', '', total_rate).center(terminal_size))
        print('------------------------------------------------'.center(terminal_size))
        qnty = int(item[1][1])
        try:
            db_data = (str(uuid.uuid4().fields[-1])[:14], cstmr_nm, cstmr_phn, now.strftime("%d/%m/%Y  %H:%M:%S"), str(save_item), qnty, total_rate)
            save_data_into_db(db_data)
        except Exception as e:
            print(e)
        input('\nPress Enter to Continue...')


    elif (okay.isalpha() == True):
        print('\nPlease Enter your details Properly!')
        bill_func(okay)
    elif (okay.isspace() == True):
        print('\nPlease Enter your details Properly!')
        bill_func(okay)
    elif (okay.isdigit() == True):
        print('\nPlease Enter your details Properly!')
        bill_func(okay)
    elif (okay.isdecimal() == True):
        print('\nPlease Enter your details Properly!')
        bill_func(okay)
    elif (regex.search(okay)):
        print('\nPlease Enter your details Properly!')
        bill_func(okay)
    elif (not okay):
        confirm = input('Are you sure to cancel your order? (y/n) :')
        if (confirm == 'n') or (confirm == 'N'):
            bill_func('1')
        elif (confirm == 'y') or (confirm == 'Y'):
            data.clear()
            pass


def run():
    ''' Main function which runs all functions in structered way. '''

    while True:
        try:
            show_items()
            okay = input("\nEnter '1' to print the bill or press Enter to cancel your order :")
            bill_func(okay)
        except Exception as e:
            print(e)
            data.clear()
        finally:
            data.clear()


if __name__ == "__main__":
    run()
