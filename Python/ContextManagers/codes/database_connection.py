import sqlite3

class DatabaseConnection:
    """
    A context manager for database connections.
    - Automatically opens and closes database connections
    - Handles transactions (commit on success, rollback on error)
    """
    def __init__(self, db_name):
        # Store the database name for later use
        self.db_name = db_name  
        self.conn = None
        
    def __enter__(self):
        """
        Called when entering the 'with' block.
        This method:
        1. Opens the database connection
        2. Returns the connection object for use in the 'with' block
        """
        print(f"Opening database connection to {self.db_name}")
        # sqlite3.connect creates a connection to the database
        self.conn = sqlite3.connect(self.db_name)
        return self.conn
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Called when exiting the 'with' block (in any case).
        This method:
        1. Checks if there was an exception (error)
        2. Rolls back changes if there was an error
        3. Commits changes if everything was successful
        4. Always closes the connection
        
        Parameters:
        - exc_type: The type of exception that occurred (or None if no exception)
        - exc_val: The exception object (or None)
        - exc_tb: The traceback object (or None)
        """
        if self.conn:
            if exc_type:  # If an exception/error occurred in the 'with' block
                print("Error occurred! Rolling back changes...")
                # rollback() undoes all changes made in the current transaction
                self.conn.rollback()
            else:  # If everything went well (no exceptions)
                print("Operations successful! Saving changes...")
                # commit() saves all changes made in the current transaction
                self.conn.commit()
                
            print("Closing database connection")
            # Always close the connection to free up resources
            self.conn.close()
            
        # Return False to let exceptions propagate (be raised)
        # Return True would suppress the exception
        return False

# Simple usage example with an in-memory database (no file needed)
with DatabaseConnection(':memory:') as conn:
    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()
    
    print("Creating a table...")
    # Create a simple table to store people
    cursor.execute('''
    CREATE TABLE people (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )''')
    
    print("Adding a person to the database...")
    # Insert a person into the table
    cursor.execute('INSERT INTO people (name, age) VALUES (?, ?)', 
                  ('John', 25))
    
    print("Checking if the person was added...")
    # Verify the person was added
    cursor.execute('SELECT * FROM people')
    result = cursor.fetchone()  # Get the first row
    print(f"Person in database: {result}")
    
# When this block ends:
# 1. The __exit__ method is called automatically
# 2. Changes are committed (saved) if no errors occurred
# 3. The connection is closed
print("Outside the with block - connection is already closed")