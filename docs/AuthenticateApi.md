# pymetquay.AuthenticateApi

All URIs are relative to *https://metquayappurl.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_access_token**](AuthenticateApi.md#get_access_token) | **POST** /authenticate | Authenticate and obtain access token


# **get_access_token**
> AuthenticationResponse get_access_token(authentication_request)

Authenticate and obtain access token

Authenticates client application using pre-provisioned access/secret keys.

**Token Expiry:** 15 minutes (900 seconds)
**Rate Limit:** Not applied to this endpoint

**Headers Required in Subsequent Calls:**
`Authorization: Bearer {accessToken}`


### Example


```python
import pymetquay
from pymetquay.models.authentication_request import AuthenticationRequest
from pymetquay.models.authentication_response import AuthenticationResponse
from pymetquay.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://metquayappurl.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pymetquay.Configuration(
    host = "https://metquayappurl.com/api/v1"
)


# Enter a context with an instance of the API client
with pymetquay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pymetquay.AuthenticateApi(api_client)
    authentication_request = pymetquay.AuthenticationRequest() # AuthenticationRequest | 

    try:
        # Authenticate and obtain access token
        api_response = api_instance.get_access_token(authentication_request)
        print("The response of AuthenticateApi->get_access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticateApi->get_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authentication_request** | [**AuthenticationRequest**](AuthenticationRequest.md)|  | 

### Return type

[**AuthenticationResponse**](AuthenticationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Authentication successful |  -  |
**400** | Bad request - validation error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

