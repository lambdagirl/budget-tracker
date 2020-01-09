import sqlite3;
import csv;
import sys;
def ae_csv(filename):
    ## Connect to the database
    try:
        conn = sqlite3.connect("bank.db");            # Get a connection object for the database
        conn.execute('PRAGMA foreign_keys = ON;');  # Turn on foreign key constraints
        csr = conn.cursor();                        # Get a cursor object for the connection
        print("connection successful, database opened!")
        # sql="DROP TABLE IF EXISTS records;"
        # csr.execute(sql)
    except Exception as e:
        print("Error connecting to database: ", e);  # Print error message
        sys.exit(); # Fatal Error

    try:
        v_sql='''CREATE TABLE records
                    (date TEXT NOT NULL,
                    Reference_number TEXT UNIQUE,
                    Payee TEXT NOT NULL,
                    Card_number TEXT NOT NULL,
                    Amount REAL NOT NULL,
                    Category TEXT,
                    Bank Text
        );'''
        csr.execute(v_sql)
        print("Table created successfully, record has been inserted successfully!")
    except Exception as e:
        print("Error create table: ", e);   # Print error message
        #sys.exit(); # Fatal Error
## Open the orders csv file
    try:
        f = open(filename, newline='');     # Open the file – default for reading
        r = csv.DictReader(f);                  # Return a dictionary reader iterator for the file
        print("\n csv file openned successfully")
    except Exception as e:
        print("Error opening csv file: ", e);   # Print error message
        sys.exit(); # Fatal Error

    ## --------------------------------------
    ## Loop through the orders csv file and insert each row in the table
    ## File title line: ord_nbr, prod_nbr, ord_qty, ord_date
    for d_row in r: # Loop on each row in the file into a list
        t_row = (d_row['Date'], d_row['Reference'], d_row['Description'],  d_row['Card Number'],float(d_row['Amount']),d_row['Category']);

        conn.execute('BEGIN TRANSACTION'); # Start transaction
        try:
            sql = 'SELECT Reference_number FROM records WHERE Reference_number = ?';
            csr.execute(sql,(t_row[1],) );
            t_id = csr.fetchone();  # Get the id in a tuple if exists (only 0 or 1 tuples returned)
            if t_id == None:        # Product number does not exist in products
                v_sql = '''INSERT INTO records (date, reference_number, payee, card_number, amount,category ,bank)
                                     VALUES (?,?,?,?,?,?,"American Express");'''
                conn.execute(v_sql, (t_row));
                sql = 'INSERT INTO records (reference_number, category) VALUES (?,?);'
                print("Record inserted!");   # Print error message
            else:
                sql = 'UPDATE records SET category = ? WHERE reference_number = ?';
                csr.execute(sql, (t_row[4], t_id[0]));
                print("Record already in!");   # Print error message
            conn.commit();      # Commit the insert or update

        except Exception as e:
            print("Error insert\\update of boas: ", t_row[0], e);  # Print error message
            conn.rollback();   # Rollback this transaction
    f.close();  # Close the file
