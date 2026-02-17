"""List customers with pagination support."""

from pymetquay import MetquayClient


def main():
    with MetquayClient() as client:
        # Single page
        print("--- First 5 customers ---")
        customers = client.list_customers(limit=5)
        for c in customers:
            print(f"  [{c.id}] {c.company_name} ({c.company_code})")

        # All customers
        print("\n--- All customers (paginate_all=True) ---")
        all_customers = client.list_customers(paginate_all=True)
        print(f"Total customers: {len(all_customers)}")
        for c in all_customers:
            print(f"  [{c.id}] {c.company_name}")


if __name__ == "__main__":
    main()
