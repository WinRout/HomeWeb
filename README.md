
# Property Scraper

This program scrapes property listings from **Spitogatos** and **XE**, stores the data in a SQLite database, and outputs new and modified properties to a text file. It also tracks the last execution time in the database.

---

## Features
- Fetches property listings from Spitogatos and XE.
- Stores property data (ID, URL, and last modified date) in a SQLite database.
- Identifies new and modified properties.
- Outputs results to a text file with a timestamped filename.
- Configurable filters for both Spitogatos and XE.

---

## Requirements
- Python 3.8 or higher
- Libraries: `requests`, `beautifulsoup4`, `sqlite3`

---

## Installation

### 1. Install Python
- **macOS/Linux**: Python is usually pre-installed. Check your version:
  ```bash
  python3 --version
  ```
  If Python is not installed, download it from python.org.

- **Windows**: Download and install Python from python.org. Make sure to check the box to add Python to your PATH during installation.

### 2. Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/WinRout/HomeWeb.git
cd HomeWeb
```

### 3. Install Dependencies
Install the required Python libraries using pip:
```bash
pip install -r requirements.txt
```

## Configuration
### 1. Edit `config.py`
The `config.py` file contains filters for Spitogatos and XE. You can modify these filters to customize the search results.

#### Spitogatos Filters
```python
SPITOGATOS_FILTERS = {
    "listingType": "sale",  # Type of listing (e.g., "sale" or "rent")
    "category": "residential",  # Property category (e.g., "residential")
    "garage": "true",  # Include properties with a garage
    "balcony": "true",  # Include properties with a balcony
    "elevator": "true",  # Include properties with an elevator
    "priceHigh": 340000,  # Maximum price
    "livingAreaLow": 90,  # Minimum living area (in square meters)
    "roomsLow": 3,  # Minimum number of rooms
    "floorNumberLow": 2,  # Minimum floor number
    "constructionYearLow": 1995,  # Minimum construction year
    "areaIDs[]": 2101,  # Area ID (e.g., 2101 for Athens)
    "sortBy": "datemodified",  # Sort by last modified date
    "sortOrder": "desc",  # Sort order (descending)
    "offset": 0  # Pagination offset
}
```

#### XE Filters
```python
XE_FILTERS = {
    "transaction_name": "buy",  # Type of transaction (e.g., "buy" or "rent")
    "item_type": "re_residence",  # Property type (e.g., "re_residence")
    "maximum_price": 340000,  # Maximum price
    "minimum_size": 90,  # Minimum size (in square meters)
    "minimum_bedrooms": 3,  # Minimum number of bedrooms
    "minimum_construction_year": 1995,  # Minimum construction year
    "minimum_level": "L2",  # Minimum floor level
    "has_parking": "true",  # Include properties with parking
    "publication_age": 10,  # Maximum publication age (in days)
    "sorting": "property_area_in_sq_m_desc",  # Sort by property area (descending)
    "geo_lat_from": 38.02412646276717,  # Latitude range (start)
    "geo_lng_from": 23.847762737483777,  # Longitude range (start)
    "geo_lat_to": 37.99449479261578,  # Latitude range (end)
    "geo_lng_to": 23.805127301826644,  # Longitude range (end)
    "maximum_price_per_unit_area": 340000  # Maximum price per unit area
}
```

## Setup
### 1. Initialize the Database
Run the following command to set up the SQLite database:
```bash
python main.py
```
This will create a `properties.db` file in the project directory.

## Execution
### 1. Run the Script
Execute the script to fetch and process property data:
```bash
python main.py
```

### 2. Check the Output
- The script will print the results to the console.
- It will also save the results to a text file named `output_YYYY-MM-DDTHH-MM-SS.txt` in the project directory.

## File Structure
```
property-scraper/
config.py                # Configuration file for filters
database.py              # Database setup and operations
fetchers.py              # Functions to fetch and parse data
main.py                  # Main script to run the program
utils.py                 # Utility functions (e.g., printing results)
requirements.txt         # List of Python dependencies
README.md                # This file
outputs                  # Directory of stored execution outputs
```

## Requirements File
The `requirements.txt` file lists all the Python libraries required for the project:
```
requests==2.31.0
beautifulsoup4==4.12.2
```

## Troubleshooting
### 1. Bot Detection
If the script fails to fetch data, it might be due to bot detection. Try:
- Reducing the frequency of script execution if spitogatos does not work.
- Visiting the xe link to execute recaptcha because it has bot detection.

### 2. Database Issues
If the database becomes corrupted, delete the `properties.db` file and rerun the script to recreate it.
