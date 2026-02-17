# WorkRequest

Request payload for creating or updating a work

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_instrument_id** | **int** | Numeric ID of the customer instrument being calibrated/tested | 
**in_date** | **datetime** | Date and time when instrument was received for work | [optional] 
**accreditation** | **bool** | true for ISO 17025 accredited work, false for non-accredited | [optional] [default to False]
**compliance_required** | **bool** | true if regulatory compliance verification is required | [optional] [default to False]
**site_job** | **bool** | true for on-site work at customer facility, false for in-lab | [optional] [default to False]
**outsource** | **bool** | true if work is subcontracted to external provider | [optional] [default to False]
**customer_specific_requirements** | **str** | Special requirements or instructions from customer | [optional] 
**scope** | **str** | Detailed description of work to be performed | [optional] 
**certificate_address** | **str** | Complete address to be printed on calibration certificate | [optional] 
**remarks** | **str** | General remarks about the work order | [optional] 
**work_flow_type** | **str** | Type of workflow to apply | [optional] [default to 'Calibration']
**delivery_date** | **datetime** | Target completion and delivery date | [optional] 
**sales_order_no** | **str** | Customer purchase order or sales order reference | [optional] 
**workspace_code** | **str** | Workspace code (required only if workspace feature is enabled) | [optional] 
**sub_con_details** | **str** | Additional details for subcontracted work | [optional] 

## Example

```python
from pymetquay import WorkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkRequest from a JSON string
work_request_instance = WorkRequest.from_json(json)
# print the JSON string representation of the object
print(WorkRequest.to_json())

# convert the object into a dict
work_request_dict = work_request_instance.to_dict()
# create an instance of WorkRequest from a dict
work_request_from_dict = WorkRequest.from_dict(work_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


