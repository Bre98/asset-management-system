# IT Asset Management System

## Overview

The IT Asset Management System is a Python-based tool designed to help organizations track and manage their hardware and software assets. The system uses an SQLite database to store asset information, making it lightweight and easy to deploy. It provides a simple command-line interface for adding, viewing, updating, and deleting hardware and software assets.

This tool is ideal for small to medium-sized IT environments where a simple, yet effective, asset tracking solution is needed.

---

## Features

- Hardware Asset Tracking:
  - Track hardware assets such as laptops, servers, and desktops.
  - Store details like asset name, type, serial number, purchase date, and location.

- Software Asset Tracking:
  - Track software assets such as installed applications.
  - Store details like software name, version, license key, and the hardware it's installed on.

- User-Friendly Interface:
  - Simple text-based menu for easy interaction.
  - No complex setup or configuration required.

- SQLite Database:
  - Lightweight and portable database for storing asset information.
  - No need for a separate database server.

---

## Prerequisites

- Python 3.x: Ensure Python 3.x is installed on your system.
- SQLite: The script uses SQLite, which is included with Python by default.

---

## Installation

1. Clone the Repository:
   ```
   git clone https://github.com/yourusername/it-asset-management.git
   ```
2. Navigate to the Project Directory:
   ```
    cd it-asset-management
   ```
3. Run the Script:
   ```
    python3 it_asset_management.py 
   ```

## Usage
Running the Script

Run the script using the following command:
```
python3 it_asset_management.py
```
### Main Menu Options

The script provides a menu with the following options:

1. Add Hardware Asset:
   - Add a new hardware asset (e.g., laptop, server) to the database.

2. Add Software Asset:
   - Add a new software asset (e.g., Microsoft Office) to the database.

3. View Hardware Assets:
   - Display a list of all hardware assets in the database.

4. View Software Assets:
   - Display a list of all software assets in the database.

5. Update Hardware Asset:
   - Update the details of an existing hardware asset.

6. Update Software Asset:
   - Update the details of an existing software asset.

7. Delete Hardware Asset:
   - Delete a hardware asset from the database.

8. Delete Software Asset:
   - Delete a software asset from the database.

9. Exit:
   - Exit the program.

## Database Schema
The system uses an SQLite database (it_assets.db) with the following tables:
### Hardware Assets Table
| Column Name | Data Type | Description |
| ----------- | ---------- | -------- |
| id | INTEGER | Primary Key (Auto-increment) |
| asset_name | TEXT | Name of the hardware asset |
| asset_type | TEXT | Type of asset (e.g., Laptop) |
| serial_number | TEXT | Serial number of the asset |
| purchase_date | TEXT | Purchase date (YYYY-MM-DD) |
| location | TEXT | Location of the asset |

### Software Assets Table
| Column Name | Data Type | Description |
| ----------- | ---------- | -------- |
| id | INTEGER | Primary Key (Auto-increment) |
| software_name | TEXT | Name of the software |
| version | TEXT | Version of the software |
| license_key | TEXT | License key for the software |
| installed_on_hardware_id | INTEGER | Foreign Key (Hardware Assets) |

## Troubleshooting

### Database Not Created:
- Ensure the script has write permissions in the directory where it is running.
- Check for any errors in the terminal output.

### SQLite Errors:
- Ensure SQLite is installed and accessible on your system.
- If the database becomes corrupted, delete the `it_assets.db` file and rerun the script to create a new one.

### Python Not Found:
- Ensure Python 3.x is installed and accessible from the command line.

## Contributing

Contributions are welcome! If you have suggestions for improvements or encounter any issues, please feel free to:
- Open an issue on GitHub.
- Submit a pull request with your changes.

## License

This project is licensed under the **MIT License**. See the LICENSE file for details.
