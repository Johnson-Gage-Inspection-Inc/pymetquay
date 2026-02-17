# pymetquay

Python SDK for the Metquay CRUD API. Provides a high-level `MetquayClient` with automatic authentication, token refresh, and pagination, built on top of a generated OpenAPI client.

## Installation

```sh
pip install -e .
```

## Quick Start

1. Create a `.env` file (or set environment variables):

```
METQUAY_ACCESS_KEY=your_access_key_here
METQUAY_SECRET_KEY=your_secret_key_here
METQUAY_HOST=johnsongage.metquay.co
```

2. Use the client:

```python
from pymetquay import MetquayClient

with MetquayClient() as client:
    # Authentication is automatic
    customers = client.list_customers(limit=10)
    for c in customers:
        print(c.company_name)
```

## Configuration

`MetquayClient` accepts optional keyword arguments, falling back to environment variables:

| Parameter | Env Var (primary) | Env Var (fallback) | Default |
|-----------|------------------|--------------------|---------|
| `access_key` | `METQUAY_ACCESS_KEY` | `ACCESS_KEY` | — |
| `secret_key` | `METQUAY_SECRET_KEY` | `SECRET_KEY` | — |
| `host` | `METQUAY_HOST` | `HOST` | `johnsongage.metquay.co` |

## Usage

### Customers

```python
from pymetquay import MetquayClient, CustomerRequest

with MetquayClient() as client:
    # List customers (with automatic pagination)
    all_customers = client.list_customers(paginate_all=True)

    # List with manual pagination
    page = client.list_customers(first=0, limit=25)

    # Create a customer
    result = client.create_customer(CustomerRequest(company_name="Acme Corp"))

    # Update a customer
    client.update_customer(metquay_id=123, request=CustomerRequest(company_name="Acme Inc"))

    # Delete a customer
    client.delete_customer(metquay_id=123)
```

### Customer Instruments

```python
from pymetquay import MetquayClient, CustomerInstrumentRequest

with MetquayClient() as client:
    instruments = client.list_instruments(limit=10)
    result = client.create_instrument(CustomerInstrumentRequest(...))
    client.update_instrument(metquay_id=456, request=CustomerInstrumentRequest(...))
    client.delete_instrument(metquay_id=456)
```

### Works

```python
from pymetquay import MetquayClient, WorkRequest

with MetquayClient() as client:
    works = client.list_works(limit=10)
    result = client.create_work(WorkRequest(...))
    client.update_work(metquay_id=789, request=WorkRequest(...))
```

### Instrument Categories

```python
from pymetquay import MetquayClient, InstrumentCategoryRequest

with MetquayClient() as client:
    # Note: the API does not provide a list endpoint for instrument categories
    result = client.create_instrument_category(InstrumentCategoryRequest(...))
    client.update_instrument_category(metquay_id=101, request=InstrumentCategoryRequest(...))
    client.delete_instrument_category(metquay_id=101)
```

### Automatic Pagination

Pass `paginate_all=True` to any list method to fetch all pages automatically:

```python
all_customers = client.list_customers(paginate_all=True)
all_instruments = client.list_instruments(paginate_all=True)
all_works = client.list_works(paginate_all=True)
```

## API Endpoints

All URIs are relative to `https://{host}/api/v1`

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthenticateApi* | [**get_access_token**](docs/AuthenticateApi.md#get_access_token) | **POST** /authenticate | Authenticate and obtain access token
*CustomerinstrumentsApi* | [**create_customer_instrument**](docs/CustomerinstrumentsApi.md#create_customer_instrument) | **POST** /customer-instrument-details | Register a new customer instrument
*CustomerinstrumentsApi* | [**delete_customer_instrument**](docs/CustomerinstrumentsApi.md#delete_customer_instrument) | **DELETE** /customer-instrument-details/{metquayId} | Delete a customer instrument
*CustomerinstrumentsApi* | [**get_customer_instruments**](docs/CustomerinstrumentsApi.md#get_customer_instruments) | **GET** /customer-instrument-details | Get paginated list of customer instruments
*CustomerinstrumentsApi* | [**update_customer_instrument**](docs/CustomerinstrumentsApi.md#update_customer_instrument) | **PUT** /customer-instrument-details/{metquayId} | Update a customer instrument
*CustomersApi* | [**create_customer**](docs/CustomersApi.md#create_customer) | **POST** /customers | Create a new customer
*CustomersApi* | [**delete_customer**](docs/CustomersApi.md#delete_customer) | **DELETE** /customers/{metquayId} | Delete a customer
*CustomersApi* | [**get_customers**](docs/CustomersApi.md#get_customers) | **GET** /customers | Get paginated list of customers
*CustomersApi* | [**update_customer**](docs/CustomersApi.md#update_customer) | **PUT** /customers/{metquayId} | Update an existing customer
*InstrumentcategoriesApi* | [**create_instrument_category**](docs/InstrumentcategoriesApi.md#create_instrument_category) | **POST** /instrument-categories | Create a new instrument category
*InstrumentcategoriesApi* | [**delete_instrument_category**](docs/InstrumentcategoriesApi.md#delete_instrument_category) | **DELETE** /instrument-categories/{metquayId} | Delete an instrument category
*InstrumentcategoriesApi* | [**update_instrument_category**](docs/InstrumentcategoriesApi.md#update_instrument_category) | **PUT** /instrument-categories/{metquayId} | Update an instrument category
*WorksApi* | [**create_work**](docs/WorksApi.md#create_work) | **POST** /works | Create a new work
*WorksApi* | [**get_works**](docs/WorksApi.md#get_works) | **GET** /works | Get paginated list of works
*WorksApi* | [**update_work**](docs/WorksApi.md#update_work) | **PUT** /works/{metquayId} | Update an existing work

## Models

 - [AuthenticationRequest](docs/AuthenticationRequest.md)
 - [AuthenticationResponse](docs/AuthenticationResponse.md)
 - [CreatedResponse](docs/CreatedResponse.md)
 - [CustomerInstrumentRequest](docs/CustomerInstrumentRequest.md)
 - [CustomerInstrumentResponse](docs/CustomerInstrumentResponse.md)
 - [CustomerRequest](docs/CustomerRequest.md)
 - [CustomerResponse](docs/CustomerResponse.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [InstrumentCategoryRequest](docs/InstrumentCategoryRequest.md)
 - [WorkRequest](docs/WorkRequest.md)
 - [WorkResponse](docs/WorkResponse.md)

## Authentication

The SDK uses Bearer authentication (JWT). Tokens are valid for 15 minutes and are automatically refreshed by `MetquayClient`.

## Rate Limiting

- **100 requests per minute** per API client
- Exceeding limit returns 429 Too Many Requests

## Tests

```sh
pytest tests/ -v
```

## Requirements

Python 3.9+

## Author

support@metquay.atlassian.net
