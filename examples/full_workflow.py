"""Full read-only workflow: authenticate, list customers, instruments, works."""

from pymetquay import ApiException, MetquayClient


def main():
    with MetquayClient() as client:
        # Auth happens automatically on first API call
        print("=== Customers ===")
        customers = client.list_customers(limit=3)
        for c in customers:
            print(f"  [{c.id}] {c.company_name}")

        print("\n=== Customer Instruments ===")
        instruments = client.list_instruments(limit=3)
        for i in instruments:
            print(f"  [{i.id}] {i.instrument_name} - {i.company_name}")

        print("\n=== Works ===")
        try:
            works = client.list_works(limit=3)
            for w in works:
                print(f"  [{w.id}] {w.work_no} - {w.customer}")
        except ApiException as e:
            print(f"  Error listing works: {e.status} {e.reason}")


if __name__ == "__main__":
    main()
