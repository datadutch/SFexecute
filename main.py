import snowflake.connector
import os
import datetime
import json

def get_conn():
    with open('sf-config.json','r') as file:
        data = json.load(file)
        user = data['user']
        password = data['password']
        account = data['account']

    conn = snowflake.connector.connect(
        user = user,
        password = password,
        account = account
        )   
    return conn 

def main(dir, ShowSuccesfull_stmt):
    from colorama import Fore, Back, Style
    from codecs import open
    from snowflake.connector.errors import DatabaseError, ProgrammingError
    print(Fore.WHITE, '\n' + 'Start running script in:' + dir)
    con = get_conn();
    icount = 0
    icountOK= 0
    icountNOK = 0
    for filename in os.listdir(dir):
        f = os.path.join(dir, filename)
        if os.path.isfile(f):
            icount += 1
            last_qry = ''
            try:
                with open(f, 'r', encoding='utf-8') as f:
                    last_qry = ''
                    print(Fore.WHITE, f.name)
                    for cur in con.execute_stream(f):
                        if ShowSuccesfull_stmt == '1':
                            last_qry += cur.query + '\n'
                    print (Fore.GREEN, 'Script succesvol gedraaid!')
                    if ShowSuccesfull_stmt == '1':
                        print(cur.query)                    
                    icountOK += 1
            except DatabaseError as db_ex:
                print(Fore.RED,  db_ex.msg)
                if ShowSuccesfull_stmt == '1':
                    print (last_qry) 
                icountNOK += 1
                pass    
    print(Fore.WHITE, 'Alle scripts gedraaid op Snowflake (' + str(icount) +' scripts: ' + str(icountOK)+' OK, ' + str(icountNOK)+ ' NOK).')

if __name__ == "__main__":
    print(datetime.datetime.now())
    main('./sql', '0')
    print(datetime.datetime.now())