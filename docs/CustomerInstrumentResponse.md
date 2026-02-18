# CustomerInstrumentResponse

Customer instrument response object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique Metquay ID of the instrument | [optional] 
**barcode** | **str** | Internal barcode identifier | [optional] 
**company_name** | **str** | Name of the customer who owns the instrument | [optional] 
**instrument_name** | **str** | Descriptive name of the instrument | [optional] 
**instrument_category** | **str** | Category of the instrument | [optional] 
**item_name** | **str** | Associated catalog item name | [optional] 
**make** | **str** | Instrument manufacturer | [optional] 
**model** | **str** | Instrument model | [optional] 
**range** | **str** | Measurement range | [optional] 
**type** | **str** | Instrument type/variant | [optional] 
**tolerance** | **str** | Accuracy tolerance specification | [optional] 
**serial_no** | **str** | Manufacturer serial number | [optional] 
**tag_no** | **str** | Internal asset tag number | [optional] 
**control_no** | **str** | Quality control tracking number | [optional] 
**calibration_frequency** | **str** | Calibration frequency value | [optional] 
**workspace_code** | **str** | Workspace code | [optional] 
**calibration_frequency_span** | **str** | Calibration frequency time unit | [optional] 
**calibrated_date** | **date** | Most recent calibration date (MM-dd-yyyy) | [optional] 
**due_date** | **date** | Next calibration due date (MM-dd-yyyy) | [optional] 
**active** | **bool** | Instrument active status | [optional] 
**parent_tag_no** | **str** | Parent instrument tag number (for component instruments) | [optional] 
**department_name** | **str** | Department or location where instrument is assigned | [optional] 
**verification_due_date** | **date** | Intermediate verification due date (MM-dd-yyyy) | [optional] 
**calibration_cost** | **float** | Cost of calibration service | [optional] 
**is_calibrated_externally** | **bool** | Indicates if calibration is performed by external vendor | [optional] 
**calibration_vendor** | **str** | Name of calibration service provider | [optional] 
**remarks** | **str** | General remarks about the instrument | [optional] 
**instrument_notes** | **str** | Internal maintenance notes | [optional] 
**is_mobile** | **bool** | Indicates if instrument is portable for field use | [optional] 
**is_calibration_required** | **bool** | Indicates if periodic calibration is required | [optional] 
**last_received_date** | **date** | Date instrument was last received (MM-dd-yyyy) | [optional] 
**last_delivered_date** | **date** | Date instrument was last delivered (MM-dd-yyyy) | [optional] 
**calibration_status** | **str** | Current calibration status | [optional] 
**received_condition** | **str** | Condition assessment when received | [optional] 
**audited_date** | **date** | Date of last quality audit (MM-dd-yyyy) | [optional] 
**certificate_url** | **str** | URL to the latest calibration certificate | [optional] 
**project_names** | **List[str]** | Associated project names or codes | [optional] 

## Example

```python
from openapi_client.models.customer_instrument_response import CustomerInstrumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerInstrumentResponse from a JSON string
customer_instrument_response_instance = CustomerInstrumentResponse.from_json(json)
# print the JSON string representation of the object
print(CustomerInstrumentResponse.to_json())

# convert the object into a dict
customer_instrument_response_dict = customer_instrument_response_instance.to_dict()
# create an instance of CustomerInstrumentResponse from a dict
customer_instrument_response_from_dict = CustomerInstrumentResponse.from_dict(customer_instrument_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


