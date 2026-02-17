# openapi_client.InstrumentcategoriesApi

All URIs are relative to *https://metquayappurl.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_instrument_category**](InstrumentcategoriesApi.md#create_instrument_category) | **POST** /instrument-categories | Create a new instrument category
[**delete_instrument_category**](InstrumentcategoriesApi.md#delete_instrument_category) | **DELETE** /instrument-categories/{metquayId} | Delete an instrument category
[**update_instrument_category**](InstrumentcategoriesApi.md#update_instrument_category) | **PUT** /instrument-categories/{metquayId} | Update an instrument category


# **create_instrument_category**
> CreatedResponse create_instrument_category(instrument_category_request)

Create a new instrument category

Creates a new instrument category.

**Uniqueness:** Category `name` must be globally unique (case-insensitive)
**Dependency:** Cannot delete categories with associated instruments


### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.created_response import CreatedResponse
from openapi_client.models.instrument_category_request import InstrumentCategoryRequest
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
    api_instance = openapi_client.InstrumentcategoriesApi(api_client)
    instrument_category_request = openapi_client.InstrumentCategoryRequest() # InstrumentCategoryRequest | 

    try:
        # Create a new instrument category
        api_response = api_instance.create_instrument_category(instrument_category_request)
        print("The response of InstrumentcategoriesApi->create_instrument_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstrumentcategoriesApi->create_instrument_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_category_request** | [**InstrumentCategoryRequest**](InstrumentCategoryRequest.md)|  | 

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
**201** | Instrument category created successfully |  -  |
**400** | Bad request - validation error |  -  |
**401** | Unauthorized - missing or invalid token |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**409** | Conflict - duplicate or dependency violation |  -  |
**422** | Unprocessable entity - business rule violation |  -  |
**429** | Too Many Requests - rate limit exceeded (100/minute) |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_instrument_category**
> delete_instrument_category(metquay_id)

Delete an instrument category

Permanently deletes an instrument category.

**Required:** No instruments can be assigned to this category
**Action:** Reassign or delete all instruments in this category first


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
    api_instance = openapi_client.InstrumentcategoriesApi(api_client)
    metquay_id = 10427 # int | Numeric ID of the resource in Metquay system

    try:
        # Delete an instrument category
        api_instance.delete_instrument_category(metquay_id)
    except Exception as e:
        print("Exception when calling InstrumentcategoriesApi->delete_instrument_category: %s\n" % e)
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
**200** | Instrument category deleted successfully |  -  |
**400** | Bad request - validation error |  -  |
**401** | Unauthorized - missing or invalid token |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**404** | Not found - resource does not exist |  -  |
**409** | Conflict - duplicate or dependency violation |  -  |
**422** | Unprocessable entity - business rule violation |  -  |
**429** | Too Many Requests - rate limit exceeded (100/minute) |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_instrument_category**
> update_instrument_category(metquay_id, instrument_category_request)

Update an instrument category

Updates an existing instrument category.

**Restriction:** Cannot update if category has associated instruments
**Workaround:** 
1. Reassign instruments to different category
2. Update category name
3. Reassign instruments back


### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.instrument_category_request import InstrumentCategoryRequest
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
    api_instance = openapi_client.InstrumentcategoriesApi(api_client)
    metquay_id = 10427 # int | Numeric ID of the resource in Metquay system
    instrument_category_request = openapi_client.InstrumentCategoryRequest() # InstrumentCategoryRequest | 

    try:
        # Update an instrument category
        api_instance.update_instrument_category(metquay_id, instrument_category_request)
    except Exception as e:
        print("Exception when calling InstrumentcategoriesApi->update_instrument_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metquay_id** | **int**| Numeric ID of the resource in Metquay system | 
 **instrument_category_request** | [**InstrumentCategoryRequest**](InstrumentCategoryRequest.md)|  | 

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
**200** | Instrument category updated successfully |  -  |
**400** | Bad request - validation error |  -  |
**401** | Unauthorized - missing or invalid token |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**404** | Not found - resource does not exist |  -  |
**409** | Conflict - duplicate or dependency violation |  -  |
**422** | Unprocessable entity - business rule violation |  -  |
**429** | Too Many Requests - rate limit exceeded (100/minute) |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

