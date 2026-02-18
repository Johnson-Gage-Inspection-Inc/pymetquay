# InstrumentCategoryRequest

Request payload for creating or updating an instrument category

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Instrument category name - must be unique across the system | 
**description** | **str** | Detailed description of the instrument category | [optional] 

## Example

```python
from openapi_client.models.instrument_category_request import InstrumentCategoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentCategoryRequest from a JSON string
instrument_category_request_instance = InstrumentCategoryRequest.from_json(json)
# print the JSON string representation of the object
print(InstrumentCategoryRequest.to_json())

# convert the object into a dict
instrument_category_request_dict = instrument_category_request_instance.to_dict()
# create an instance of InstrumentCategoryRequest from a dict
instrument_category_request_from_dict = InstrumentCategoryRequest.from_dict(instrument_category_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


