# openapi_client.CustomersApi

All URIs are relative to *https://metquayappurl.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_customer**](CustomersApi.md#create_customer) | **POST** /customers | Create a new customer
[**delete_customer**](CustomersApi.md#delete_customer) | **DELETE** /customers/{metquayId} | Delete a customer
[**get_customers**](CustomersApi.md#get_customers) | **GET** /customers | Get paginated list of customers
[**update_customer**](CustomersApi.md#update_customer) | **PUT** /customers/{metquayId} | Update an existing customer


# **create_customer**
> CreatedResponse create_customer(customer_request)

Create a new customer

Creates a new customer record. Customers own calibration instruments.

**Auto-generation:** `companyCode` auto-generated if not provided
**Uniqueness:** `companyName` must be unique
**Default Address:** Billing address = Primary = Certificate address


### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.created_response import CreatedResponse
from openapi_client.models.customer_request import CustomerRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://metquayappurl.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://metquayappurl.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CustomersApi(api_client)
    customer_request = openapi_client.CustomerRequest() # CustomerRequest | 

    try:
        # Create a new customer
        api_response = api_instance.create_customer(customer_request)
        print("The response of CustomersApi->create_customer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->create_customer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_request** | [**CustomerRequest**](CustomerRequest.md)|  | 

### Return type

[**CreatedResponse**](CreatedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Customer created successfully |  -  |
**400** | Bad request - validation error |  -  |
**401** | Unauthorized - missing or invalid token |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**409** | Conflict - duplicate or dependency violation |  -  |
**422** | Unprocessable entity - business rule violation |  -  |
**429** | Too Many Requests - rate limit exceeded (100/minute) |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_customer**
> delete_customer(metquay_id)

Delete a customer

Permanently deletes a customer record.

**Restrictions - Cannot delete if customer has:**
- Any associated instruments
- Any active or historical works

**Alternative:** Set `isInactive: true` instead of deleting


### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://metquayappurl.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://metquayappurl.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CustomersApi(api_client)
    metquay_id = 10427 # int | Numeric ID of the resource in Metquay system

    try:
        # Delete a customer
        api_instance.delete_customer(metquay_id)
    except Exception as e:
        print("Exception when calling CustomersApi->delete_customer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metquay_id** | **int**| Numeric ID of the resource in Metquay system | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Customer deleted successfully |  -  |
**400** | Bad request - validation error |  -  |
**401** | Unauthorized - missing or invalid token |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**404** | Not found - resource does not exist |  -  |
**409** | Conflict - duplicate or dependency violation |  -  |
**422** | Unprocessable entity - business rule violation |  -  |
**429** | Too Many Requests - rate limit exceeded (100/minute) |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customers**
> List[CustomerResponse] get_customers(workspace_code=workspace_code, first=first, limit=limit)

Get paginated list of customers

Retrieves a paginated list of customers.

**Pagination:**
- Use `first` and `limit` to control result set

**Workspace:**
- `workspaceCode` is optional - only include if workspace feature is enabled


### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.customer_response import CustomerResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://metquayappurl.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://metquayappurl.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CustomersApi(api_client)
    workspace_code = 'workspace_code_example' # str | Workspace code (optional - only required if workspace feature is enabled) (optional)
    first = 0 # int | Starting index for pagination (optional) (default to 0)
    limit = 50 # int | Number of records to return (default 50) (optional) (default to 50)

    try:
        # Get paginated list of customers
        api_response = api_instance.get_customers(workspace_code=workspace_code, first=first, limit=limit)
        print("The response of CustomersApi->get_customers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->get_customers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_code** | **str**| Workspace code (optional - only required if workspace feature is enabled) | [optional] 
 **first** | **int**| Starting index for pagination | [optional] [default to 0]
 **limit** | **int**| Number of records to return (default 50) | [optional] [default to 50]

### Return type

[**List[CustomerResponse]**](CustomerResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - returns paginated customers |  -  |
**400** | Bad request - validation error |  -  |
**401** | Unauthorized - missing or invalid token |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**429** | Too Many Requests - rate limit exceeded (100/minute) |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_customer**
> update_customer(metquay_id, customer_request)

Update an existing customer

Updates an existing customer record.

**Full Replacement:** All fields not included in request will be reset to null/default
**Immutable Fields:** `companyCode` cannot be modified after creation
**Type Change:** Cannot change `isPerson` (company/individual) after creation


### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.customer_request import CustomerRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://metquayappurl.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://metquayappurl.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CustomersApi(api_client)
    metquay_id = 10427 # int | Numeric ID of the resource in Metquay system
    customer_request = openapi_client.CustomerRequest() # CustomerRequest | 

    try:
        # Update an existing customer
        api_instance.update_customer(metquay_id, customer_request)
    except Exception as e:
        print("Exception when calling CustomersApi->update_customer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metquay_id** | **int**| Numeric ID of the resource in Metquay system | 
 **customer_request** | [**CustomerRequest**](CustomerRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Customer updated successfully |  -  |
**400** | Bad request - validation error |  -  |
**401** | Unauthorized - missing or invalid token |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**404** | Not found - resource does not exist |  -  |
**409** | Conflict - duplicate or dependency violation |  -  |
**422** | Unprocessable entity - business rule violation |  -  |
**429** | Too Many Requests - rate limit exceeded (100/minute) |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

