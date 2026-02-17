# openapi_client.CustomerinstrumentsApi

All URIs are relative to *https://metquayappurl.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_customer_instrument**](CustomerinstrumentsApi.md#create_customer_instrument) | **POST** /customer-instrument-details | Register a new customer instrument
[**delete_customer_instrument**](CustomerinstrumentsApi.md#delete_customer_instrument) | **DELETE** /customer-instrument-details/{metquayId} | Delete a customer instrument
[**get_customer_instruments**](CustomerinstrumentsApi.md#get_customer_instruments) | **GET** /customer-instrument-details | Get paginated list of customer instruments
[**update_customer_instrument**](CustomerinstrumentsApi.md#update_customer_instrument) | **PUT** /customer-instrument-details/{metquayId} | Update a customer instrument


# **create_customer_instrument**
> CreatedResponse create_customer_instrument(customer_instrument_request)

Register a new customer instrument

Registers a new instrument owned by a customer.

**Required References:**
- Existing customer (`companyId`)
- Existing instrument category (`instrumentCategoryName`)

**Calibration Scheduling:**
If `calibrationFrequency` + `calibrationFrequencySpan` provided:
- `dueDate` auto-calculated from `calibratedDate` (defaults to creation date)

**Uniqueness:** Serial/Tag number combinations should be unique per customer


### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.created_response import CreatedResponse
from openapi_client.models.customer_instrument_request import CustomerInstrumentRequest
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
    api_instance = openapi_client.CustomerinstrumentsApi(api_client)
    customer_instrument_request = openapi_client.CustomerInstrumentRequest() # CustomerInstrumentRequest | 

    try:
        # Register a new customer instrument
        api_response = api_instance.create_customer_instrument(customer_instrument_request)
        print("The response of CustomerinstrumentsApi->create_customer_instrument:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomerinstrumentsApi->create_customer_instrument: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_instrument_request** | [**CustomerInstrumentRequest**](CustomerInstrumentRequest.md)|  | 

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
**201** | Customer instrument created successfully |  -  |
**400** | Bad request - validation error |  -  |
**401** | Unauthorized - missing or invalid token |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**409** | Conflict - duplicate or dependency violation |  -  |
**422** | Unprocessable entity - business rule violation |  -  |
**429** | Too Many Requests - rate limit exceeded (100/minute) |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_customer_instrument**
> delete_customer_instrument(metquay_id)

Delete a customer instrument

Permanently deletes a customer instrument.

**Restrictions - Cannot delete if instrument has:**
- Any associated works (active or historical)
- Any child instruments (parentInstrumentId references this instrument)

**Alternative:** Set `isActive: false` instead of deleting


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
    api_instance = openapi_client.CustomerinstrumentsApi(api_client)
    metquay_id = 10427 # int | Numeric ID of the resource in Metquay system

    try:
        # Delete a customer instrument
        api_instance.delete_customer_instrument(metquay_id)
    except Exception as e:
        print("Exception when calling CustomerinstrumentsApi->delete_customer_instrument: %s\n" % e)
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
**200** | Customer instrument deleted successfully |  -  |
**400** | Bad request - validation error |  -  |
**401** | Unauthorized - missing or invalid token |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**404** | Not found - resource does not exist |  -  |
**409** | Conflict - duplicate or dependency violation |  -  |
**422** | Unprocessable entity - business rule violation |  -  |
**429** | Too Many Requests - rate limit exceeded (100/minute) |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_instruments**
> List[CustomerInstrumentResponse] get_customer_instruments(workspace_code=workspace_code, first=first, limit=limit)

Get paginated list of customer instruments

Retrieves a paginated list of customer instruments.

**Pagination:**
- Use `first` and `limit` to control result set

**Workspace:**
- `workspaceCode` is optional - only include if workspace feature is enabled


### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.customer_instrument_response import CustomerInstrumentResponse
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
    api_instance = openapi_client.CustomerinstrumentsApi(api_client)
    workspace_code = 'workspace_code_example' # str | Workspace code (optional - only required if workspace feature is enabled) (optional)
    first = 0 # int | Starting index for pagination (optional) (default to 0)
    limit = 50 # int | Number of records to return (default 50) (optional) (default to 50)

    try:
        # Get paginated list of customer instruments
        api_response = api_instance.get_customer_instruments(workspace_code=workspace_code, first=first, limit=limit)
        print("The response of CustomerinstrumentsApi->get_customer_instruments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomerinstrumentsApi->get_customer_instruments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_code** | **str**| Workspace code (optional - only required if workspace feature is enabled) | [optional] 
 **first** | **int**| Starting index for pagination | [optional] [default to 0]
 **limit** | **int**| Number of records to return (default 50) | [optional] [default to 50]

### Return type

[**List[CustomerInstrumentResponse]**](CustomerInstrumentResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - returns paginated customer instruments |  -  |
**400** | Bad request - validation error |  -  |
**401** | Unauthorized - missing or invalid token |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**429** | Too Many Requests - rate limit exceeded (100/minute) |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_customer_instrument**
> update_customer_instrument(metquay_id, customer_instrument_request)

Update a customer instrument

Updates an existing customer instrument.

**Full Replacement:** All fields not included are reset
**Ownership Change:** Changing `companyId` transfers instrument to another customer
**Category Change:** May affect calibration procedures and pricing


### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.customer_instrument_request import CustomerInstrumentRequest
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
    api_instance = openapi_client.CustomerinstrumentsApi(api_client)
    metquay_id = 10427 # int | Numeric ID of the resource in Metquay system
    customer_instrument_request = openapi_client.CustomerInstrumentRequest() # CustomerInstrumentRequest | 

    try:
        # Update a customer instrument
        api_instance.update_customer_instrument(metquay_id, customer_instrument_request)
    except Exception as e:
        print("Exception when calling CustomerinstrumentsApi->update_customer_instrument: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metquay_id** | **int**| Numeric ID of the resource in Metquay system | 
 **customer_instrument_request** | [**CustomerInstrumentRequest**](CustomerInstrumentRequest.md)|  | 

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
**200** | Customer instrument updated successfully |  -  |
**400** | Bad request - validation error |  -  |
**401** | Unauthorized - missing or invalid token |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**404** | Not found - resource does not exist |  -  |
**409** | Conflict - duplicate or dependency violation |  -  |
**422** | Unprocessable entity - business rule violation |  -  |
**429** | Too Many Requests - rate limit exceeded (100/minute) |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

