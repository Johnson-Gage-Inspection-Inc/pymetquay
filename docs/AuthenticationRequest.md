# AuthenticationRequest

Authentication request payload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | **str** | API access key provided by Metquay administrator | 
**secret_key** | **str** | API secret key provided by Metquay administrator | 

## Example

```python
from openapi_client.models.authentication_request import AuthenticationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationRequest from a JSON string
authentication_request_instance = AuthenticationRequest.from_json(json)
# print the JSON string representation of the object
print(AuthenticationRequest.to_json())

# convert the object into a dict
authentication_request_dict = authentication_request_instance.to_dict()
# create an instance of AuthenticationRequest from a dict
authentication_request_from_dict = AuthenticationRequest.from_dict(authentication_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


