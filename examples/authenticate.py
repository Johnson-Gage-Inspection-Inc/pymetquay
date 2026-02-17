"""Demonstrate basic authentication with the Metquay API."""

from pymetquay import MetquayClient


def main():
    with MetquayClient() as client:
        response = client.authenticate()
        print(f"Token type : {response.token_type}")
        print(f"Expires in : {response.expires_in} seconds")
        print(f"Token (first 20 chars): {response.access_token[:20]}...")


if __name__ == "__main__":
    main()
