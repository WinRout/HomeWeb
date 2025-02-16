from config import SPITOGATOS_FILTERS, XE_FILTERS, QUERY_URL_SPITOGATOS, QUERY_URL_XE
from database import setup_database, save_properties, update_execution_time
from fetchers import fetch_data, parse_spitogatos, parse_xe
from utils import print_results

def main():
    """Main function to fetch, save, and print property data."""
    setup_database()

    # Fetch and process Spitogatos data
    spitogatos_properties = fetch_data(QUERY_URL_SPITOGATOS, params=SPITOGATOS_FILTERS, parser=parse_spitogatos)
    new_spitogatos_ids, modified_spitogatos_ids = save_properties(spitogatos_properties, 'spitogatos')

    # Fetch and process XE data
    xe_properties = fetch_data(QUERY_URL_XE, params=XE_FILTERS, parser=parse_xe)
    new_xe_ids, modified_xe_ids = save_properties(xe_properties, 'xe')

    # Prepare results for printing
    spitogatos_results = {
        "new_ids": new_spitogatos_ids,
        "modified_ids": modified_spitogatos_ids
    }
    xe_results = {
        "new_ids": new_xe_ids,
        "modified_ids": modified_xe_ids
    }

    # Print and save consolidated results
    print_results(spitogatos_results, xe_results)

    # Update the last execution time in the database
    update_execution_time()

if __name__ == "__main__":
    main()