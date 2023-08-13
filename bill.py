
from datetime import datetime
from database import save_data_into_db
import uuid, shutil

terminal_size = shutil.get_terminal_size().columns
now = datetime.now()

def bill_save_into_txt(save_data, cstmr_nm, cstmr_phn):

    f = open('GUI/data.txt', 'w')

    # Format of bill.
    print('----------------------------------------'.center(terminal_size), file = f)
    print('**** Bill ****'.center(terminal_size), file = f)
    print("** Noida's Pizza **".center(terminal_size), file = f)
    print('Sector-**'.center(terminal_size), file = f)
    print('Noida, G.B Nagar, U.P'.center(terminal_size), file = f)
    print('------------------------------------------------'.center(terminal_size), file = f)
    print(now.strftime("%d/%m/%Y  %H:%M:%S").center(terminal_size), file = f)
    print(f"Order Id : {str(uuid.uuid4().fields[-1])[:14]}".center(terminal_size), file = f)
    print(f"Name : {cstmr_nm}".center(terminal_size), file = f)
    print(f"Phone no. : {cstmr_phn}".center(terminal_size), file = f)
    print('------------------------------------------------'.center(terminal_size), file = f)

    # Calculating total rate and printing final bill.
    total_rate = 0
    s_item = []
    q_item = []
    print('{} {:<25} {:<10} {:<10}'.format('SNO', 'ORDERED ITEMS', '', 'RATE').center(terminal_size + 6), file = f)
    for i, item in enumerate(save_data.items()):
        print('{}.  {:<25} {:<10} {:<10}'.format(i+1, item[1][1], f'[x{item[1][2]}]', item[1][3]).center(terminal_size + 6), file = f)
        total_rate += int(item[1][3])
        s_item.append(item[1][1])
        q_item.append(item[1][2])
    print('======================================'.center(terminal_size + 6), file = f)
    print('{}  {:<25} {:<10} {}'.format(' ', 'Total Rate - ', '', total_rate).center(terminal_size), file = f)
    print('------------------------------------------------'.center(terminal_size), file = f)
    f.close()
    try:
        db_data = (str(uuid.uuid4().fields[-1])[:14], cstmr_nm, cstmr_phn, now.strftime("%d/%m/%Y  %H:%M:%S"), str(s_item), q_item, total_rate)
        save_data_into_db(db_data)
    except Exception as e:
        print(e)


