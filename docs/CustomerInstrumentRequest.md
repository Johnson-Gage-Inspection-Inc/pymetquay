# CustomerInstrumentRequest

Request payload for creating or updating a customer instrument

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Descriptive name of the instrument | 
**company_id** | **str** | Customer ID or code that owns this instrument | 
**serial_no** | **str** | Manufacturer&#39;s unique serial number | [optional] 
**tag_no** | **str** | Internal asset tag or tracking number | [optional] 
**make** | **str** | Instrument manufacturer or brand | [optional] 
**model** | **str** | Manufacturer&#39;s model designation | [optional] 
**range** | **str** | Measurement range specifications | [optional] 
**instrument_category_name** | **str** | Category this instrument belongs to | 
**calibration_frequency** | **str** | Numerical value for calibration frequency | [optional] 
**calibration_frequency_span** | **str** | Time unit for calibration frequency | [optional] 
**instrument_status** | **str** | Current operational status of the instrument | [optional] 
**last_received_date** | **datetime** | Date and time when instrument was last received | [optional] 
**last_delivered_date** | **datetime** | Date and time when instrument was last delivered | [optional] 
**workspace_code** | **str** | Workspace code (required only if workspace feature is enabled) | [optional] 

## Example

```python
from openapi_client.models.customer_instrument_request import CustomerInstrumentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerInstrumentRequest from a JSON string
customer_instrument_request_instance = CustomerInstrumentRequest.from_json(json)
# print the JSON string representation of the object
print(CustomerInstrumentRequest.to_json())

# convert the object into a dict
customer_instrument_request_dict = customer_instrument_request_instance.to_dict()
# create an instance of CustomerInstrumentRequest from a dict
customer_instrument_request_from_dict = CustomerInstrumentRequest.from_dict(customer_instrument_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


