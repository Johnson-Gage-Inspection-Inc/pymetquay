# WorkResponse

Work response object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique Metquay ID of the work | [optional] 
**work_no** | **str** | Unique work order number | [optional] 
**customer_instrument_id** | **int** | Numeric ID of the customer instrument | [optional] 
**in_date** | **date** | Date instrument was received | [optional] 
**accreditation** | **bool** | Indicates if work is ISO 17025 accredited | [optional] 
**compliance_required** | **bool** | Indicates if regulatory compliance verification is required | [optional] 
**site_job** | **bool** | Indicates if work was performed on-site | [optional] 
**outsource** | **bool** | Indicates if work was subcontracted | [optional] 
**customer_specific_requirements** | **str** | Customer special requirements | [optional] 
**scope** | **str** | Detailed scope of work | [optional] 
**certificate_address** | **str** | Complete address printed on certificate | [optional] 
**remarks** | **str** | Work order remarks | [optional] 
**work_flow_type** | **str** | Type of workflow performed | [optional] 
**delivery_date** | **date** | Target delivery date | [optional] 
**sales_order_no** | **str** | Customer purchase order or sales order reference | [optional] 
**workspace_code** | **str** | Workspace code | [optional] 
**sub_con_details** | **str** | Subcontractor details if outsourced | [optional] 
**customer** | **str** | Customer name | [optional] 
**instrument_name** | **str** | Instrument name | [optional] 
**instrument_serial_no** | **str** | Instrument serial number | [optional] 
**instrument_tag_no** | **str** | Instrument tag number | [optional] 
**instrument_barcode** | **str** | Instrument barcode | [optional] 
**instrument_category_name** | **str** | Instrument category | [optional] 
**item_description** | **str** | Catalog item description | [optional] 
**department_name** | **str** | Department performing the work | [optional] 
**status** | **str** | Current work status | [optional] 
**report_type** | **str** | Type of report/certificate generated | [optional] 
**accreditation_type** | **str** | Accreditation standard applied | [optional] 
**procedure** | **str** | Calibration procedure used | [optional] 
**technician** | **str** | Primary technician assigned | [optional] 
**work_date** | **date** | Date work was performed (MM-dd-yyyy) | [optional] 
**due_date** | **date** | Original due date (MM-dd-yyyy) | [optional] 
**revision_no** | **int** | Revision number of the work order | [optional] 
**certificate_no** | **str** | Generated certificate number | [optional] 
**finished_date** | **date** | Date work was completed (MM-dd-yyyy) | [optional] 
**finished_by** | **str** | Technician who completed the work | [optional] 
**sales_person** | **str** | Sales representative | [optional] 
**recommended_due_date** | **date** | Recommended next calibration due date (MM-dd-yyyy) | [optional] 
**calibrated_date** | **date** | Actual calibration date (MM-dd-yyyy) | [optional] 
**work_start_date** | **date** | Work start date (MM-dd-yyyy) | [optional] 
**customer_po_no** | **str** | Customer purchase order number | [optional] 
**so_description** | **str** | Sales order description | [optional] 
**workspace** | **str** | Workspace name | [optional] 
**job_type** | **str** | Job type classification | [optional] 

## Example

```python
from openapi_client.models.work_response import WorkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkResponse from a JSON string
work_response_instance = WorkResponse.from_json(json)
# print the JSON string representation of the object
print(WorkResponse.to_json())

# convert the object into a dict
work_response_dict = work_response_instance.to_dict()
# create an instance of WorkResponse from a dict
work_response_from_dict = WorkResponse.from_dict(work_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


