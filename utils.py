import sqlite3
from typing import List, Dict
from database import get_last_execution_time

def print_results(spitogatos_results: Dict, xe_results: Dict) -> None:
    """
    Print and save results for both Spitogatos and XE properties.
    Results are consolidated into a single output file.
    """
    last_execution_time = get_last_execution_time()
    print(f"Last executed on: {last_execution_time}\n")

    def get_urls_from_db(ids: List[str], table_name: str) -> List[str]:
        """Fetch URLs from the database for the given IDs."""
        with sqlite3.connect('properties.db') as conn:
            cursor = conn.cursor()
            placeholders = ', '.join('?' for _ in ids)
            query = f"SELECT url FROM {table_name} WHERE id IN ({placeholders})"
            cursor.execute(query, ids)
            return [row[0] for row in cursor.fetchall()]

    # Prepare the output content
    output_content = f"Last executed on: {last_execution_time}\n\n"

    # Process Spitogatos results
    if spitogatos_results["new_ids"]:
        output_content += "New properties found on Spitogatos:\n"
        urls = get_urls_from_db(spitogatos_results["new_ids"], "spitogatos")
        output_content += "\n".join(urls) + "\n\n"
    # if spitogatos_results["modified_ids"]:
    #     output_content += "Modified properties on Spitogatos:\n"
    #     urls = get_urls_from_db(spitogatos_results["modified_ids"], "spitogatos")
    #     output_content += "\n".join(urls) + "\n\n"
    # if not spitogatos_results["new_ids"] and not spitogatos_results["modified_ids"]:
    #     output_content += "No new or modified properties found on Spitogatos.\n\n"
    else:
        output_content += "No new properties found on spitogatos."

    # Process XE results
    if xe_results["new_ids"]:
        output_content += "New properties found on XE:\n"
        urls = get_urls_from_db(xe_results["new_ids"], "xe")
        output_content += "\n".join(urls) + "\n\n"
    # if xe_results["modified_ids"]:
    #     output_content += "Modified properties on XE:\n"
    #     urls = get_urls_from_db(xe_results["modified_ids"], "xe")
    #     output_content += "\n".join(urls) + "\n\n"
    # if not xe_results["new_ids"] and not xe_results["modified_ids"]:
    #     output_content += "No new or modified properties found on XE.\n\n"
    else:
        output_content += "No new properties found on XE."

    # Print to console
    print(output_content)

    # Save to file
    filename = f"outputs/output_{last_execution_time.replace(':', '-').replace('.', '-')}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(output_content)
    print(f"Results saved to {filename}")