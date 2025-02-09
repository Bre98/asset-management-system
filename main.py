import sqlite3
from datetime import datetime

# Database file name
DATABASE_FILE = "it_assets.db"

# Function to initialize the database and create tables
def initialize_database():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    # Create Hardware Assets table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS hardware_assets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            asset_name TEXT NOT NULL,
            asset_type TEXT NOT NULL,
            serial_number TEXT UNIQUE,
            purchase_date TEXT,
            location TEXT
        )
    ''')

    # Create Software Assets table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS software_assets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            software_name TEXT NOT NULL,
            version TEXT,
            license_key TEXT UNIQUE,
            installed_on_hardware_id INTEGER,
            FOREIGN KEY (installed_on_hardware_id) REFERENCES hardware_assets(id)
        )
    ''')

    conn.commit()
    conn.close()
    print("Database initialized successfully.")

# Function to add a hardware asset
def add_hardware_asset():
    asset_name = input("Enter asset name: ")
    asset_type = input("Enter asset type (e.g., Laptop, Server): ")
    serial_number = input("Enter serial number: ")
    purchase_date = input("Enter purchase date (YYYY-MM-DD): ")
    location = input("Enter location: ")

    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO hardware_assets (asset_name, asset_type, serial_number, purchase_date, location)
        VALUES (?, ?, ?, ?, ?)
    ''', (asset_name, asset_type, serial_number, purchase_date, location))
    conn.commit()
    conn.close()
    print("Hardware asset added successfully.")

# Function to add a software asset
def add_software_asset():
    software_name = input("Enter software name: ")
    version = input("Enter version: ")
    license_key = input("Enter license key: ")
    installed_on_hardware_id = input("Enter the ID of the hardware it's installed on: ")

    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO software_assets (software_name, version, license_key, installed_on_hardware_id)
        VALUES (?, ?, ?, ?)
    ''', (software_name, version, license_key, installed_on_hardware_id))
    conn.commit()
    conn.close()
    print("Software asset added successfully.")

# Function to view all hardware assets
def view_hardware_assets():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM hardware_assets")
    rows = cursor.fetchall()

    print("\nHardware Assets:")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Type: {row[2]}, Serial: {row[3]}, Purchase Date: {row[4]}, Location: {row[5]}")

    conn.close()

# Function to view all software assets
def view_software_assets():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM software_assets")
    rows = cursor.fetchall()

    print("\nSoftware Assets:")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Version: {row[2]}, License Key: {row[3]}, Installed on Hardware ID: {row[4]}")

    conn.close()

# Function to update a hardware asset
def update_hardware_asset():
    asset_id = input("Enter the ID of the hardware asset to update: ")
    asset_name = input("Enter new asset name: ")
    asset_type = input("Enter new asset type: ")
    serial_number = input("Enter new serial number: ")
    purchase_date = input("Enter new purchase date (YYYY-MM-DD): ")
    location = input("Enter new location: ")

    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE hardware_assets
        SET asset_name = ?, asset_type = ?, serial_number = ?, purchase_date = ?, location = ?
        WHERE id = ?
    ''', (asset_name, asset_type, serial_number, purchase_date, location, asset_id))
    conn.commit()
    conn.close()
    print("Hardware asset updated successfully.")

# Function to update a software asset
def update_software_asset():
    software_id = input("Enter the ID of the software asset to update: ")
    software_name = input("Enter new software name: ")
    version = input("Enter new version: ")
    license_key = input("Enter new license key: ")
    installed_on_hardware_id = input("Enter new hardware ID it's installed on: ")

    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE software_assets
        SET software_name = ?, version = ?, license_key = ?, installed_on_hardware_id = ?
        WHERE id = ?
    ''', (software_name, version, license_key, installed_on_hardware_id, software_id))
    conn.commit()
    conn.close()
    print("Software asset updated successfully.")

# Function to delete a hardware asset
def delete_hardware_asset():
    asset_id = input("Enter the ID of the hardware asset to delete: ")

    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM hardware_assets WHERE id = ?", (asset_id,))
    conn.commit()
    conn.close()
    print("Hardware asset deleted successfully.")

# Function to delete a software asset
def delete_software_asset():
    software_id = input("Enter the ID of the software asset to delete: ")

    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM software_assets WHERE id = ?", (software_id,))
    conn.commit()
    conn.close()
    print("Software asset deleted successfully.")

# Main menu
def main_menu():
    while True:
        print("\nIT Asset Management System")
        print("1. Add Hardware Asset")
        print("2. Add Software Asset")
        print("3. View Hardware Assets")
        print("4. View Software Assets")
        print("5. Update Hardware Asset")
        print("6. Update Software Asset")
        print("7. Delete Hardware Asset")
        print("8. Delete Software Asset")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_hardware_asset()
        elif choice == "2":
            add_software_asset()
        elif choice == "3":
            view_hardware_assets()
        elif choice == "4":
            view_software_assets()
        elif choice == "5":
            update_hardware_asset()
        elif choice == "6":
            update_software_asset()
        elif choice == "7":
            delete_hardware_asset()
        elif choice == "8":
            delete_software_asset()
        elif choice == "9":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Initialize the database and start the program
if __name__ == "__main__":
    initialize_database()
    main_menu()
