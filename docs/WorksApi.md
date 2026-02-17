# pymetquay.WorksApi

All URIs are relative to *https://metquayappurl.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_work**](WorksApi.md#create_work) | **POST** /works | Create a new work
[**get_works**](WorksApi.md#get_works) | **GET** /works | Get paginated list of works
[**update_work**](WorksApi.md#update_work) | **PUT** /works/{metquayId} | Update an existing work


# **create_work**
> CreatedResponse create_work(work_request)

Create a new work

Creates a calibration, testing, or evaluation work.

**Work Types (`workFlowType`):**
- `Calibration`: Adjust and verify accuracy (default)
- `Testing`: Verify performance without adjustment
- `Evaluation`: Assess condition and recommend actions

**Auto-numbering:** `workNo` auto-generated if not provided
**Required Reference:** Existing customer instrument (`customerInstrumentId`)


### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import pymetquay
from pymetquay.models.created_response import CreatedResponse
from pymetquay.models.work_request import WorkRequest
from pymetquay.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://metquayappurl.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pymetquay.Configuration(
    host = "https://metquayappurl.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = pymetquay.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pymetquay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pymetquay.WorksApi(api_client)
    work_request = pymetquay.WorkRequest() # WorkRequest | 

    try:
        # Create a new work
        api_response = api_instance.create_work(work_request)
        print("The response of WorksApi->create_work:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksApi->create_work: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_request** | [**WorkRequest**](WorkRequest.md)|  | 

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
**201** | Work created successfully |  -  |
**400** | Bad request - validation error |  -  |
**401** | Unauthorized - missing or invalid token |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**409** | Conflict - duplicate or dependency violation |  -  |
**422** | Unprocessable entity - business rule violation |  -  |
**429** | Too Many Requests - rate limit exceeded (100/minute) |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_works**
> List[WorkResponse] get_works(workspace_code=workspace_code, first=first, limit=limit)

Get paginated list of works

Retrieves a paginated list of works.

**Pagination:**
- Use `first` and `limit` to control result set

**Workspace:**
- `workspaceCode` is optional - only include if workspace feature is enabled


### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import pymetquay
from pymetquay.models.work_response import WorkResponse
from pymetquay.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://metquayappurl.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pymetquay.Configuration(
    host = "https://metquayappurl.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = pymetquay.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pymetquay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pymetquay.WorksApi(api_client)
    workspace_code = 'workspace_code_example' # str | Workspace code (optional - only required if workspace feature is enabled) (optional)
    first = 0 # int | Starting index for pagination (optional) (default to 0)
    limit = 50 # int | Number of records to return (default 50) (optional) (default to 50)

    try:
        # Get paginated list of works
        api_response = api_instance.get_works(workspace_code=workspace_code, first=first, limit=limit)
        print("The response of WorksApi->get_works:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksApi->get_works: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_code** | **str**| Workspace code (optional - only required if workspace feature is enabled) | [optional] 
 **first** | **int**| Starting index for pagination | [optional] [default to 0]
 **limit** | **int**| Number of records to return (default 50) | [optional] [default to 50]

### Return type

[**List[WorkResponse]**](WorkResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - returns paginated works |  -  |
**400** | Bad request - validation error |  -  |
**401** | Unauthorized - missing or invalid token |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**429** | Too Many Requests - rate limit exceeded (100/minute) |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_work**
> update_work(metquay_id, work_request)

Update an existing work

Updates an existing work.

**Immutable Fields:** `workNo` cannot be changed
**Status Restriction:** Cannot modify completed or cancelled works
**Reassignment:** Changing `customerInstrumentId` reassigns work to different instrument


### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import pymetquay
from pymetquay.models.work_request import WorkRequest
from pymetquay.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://metquayappurl.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pymetquay.Configuration(
    host = "https://metquayappurl.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = pymetquay.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pymetquay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pymetquay.WorksApi(api_client)
    metquay_id = 10427 # int | Numeric ID of the resource in Metquay system
    work_request = pymetquay.WorkRequest() # WorkRequest | 

    try:
        # Update an existing work
        api_instance.update_work(metquay_id, work_request)
    except Exception as e:
        print("Exception when calling WorksApi->update_work: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metquay_id** | **int**| Numeric ID of the resource in Metquay system | 
 **work_request** | [**WorkRequest**](WorkRequest.md)|  | 

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
**200** | Work updated successfully |  -  |
**400** | Bad request - validation error |  -  |
**401** | Unauthorized - missing or invalid token |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**404** | Not found - resource does not exist |  -  |
**409** | Conflict - duplicate or dependency violation |  -  |
**422** | Unprocessable entity - business rule violation |  -  |
**429** | Too Many Requests - rate limit exceeded (100/minute) |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

