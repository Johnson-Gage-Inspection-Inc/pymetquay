# CreatedResponse

Standard response for successful resource creation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metquay_id** | **int** | Unique numeric ID of the created resource | 

## Example

```python
from openapi_client.models.created_response import CreatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreatedResponse from a JSON string
created_response_instance = CreatedResponse.from_json(json)
# print the JSON string representation of the object
print(CreatedResponse.to_json())

# convert the object into a dict
created_response_dict = created_response_instance.to_dict()
# create an instance of CreatedResponse from a dict
created_response_from_dict = CreatedResponse.from_dict(created_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


