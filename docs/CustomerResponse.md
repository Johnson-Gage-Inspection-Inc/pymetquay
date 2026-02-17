# CustomerResponse

Customer response object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique Metquay ID of the customer | [optional] 
**parent_company_code** | **str** | Parent company code (if this customer is a subsidiary) | [optional] 
**company_code** | **str** | Unique identifier for the customer | [optional] 
**is_inactive** | **bool** | Customer status - false for active, true for inactive | [optional] 
**company_name** | **str** | Legal name of the customer organization | [optional] 
**email** | **str** | Primary contact email address | [optional] 
**website** | **str** | Customer website URL | [optional] 
**payment_method** | **str** | Preferred payment method | [optional] 
**phone** | **str** | Primary phone number | [optional] 
**mobile** | **str** | Mobile phone number | [optional] 
**fax** | **str** | Fax number | [optional] 
**other** | **str** | Alternate phone number | [optional] 
**activate_alerts** | **bool** | Alert notification status | [optional] 
**workspace_code** | **str** | Workspace code | [optional] 
**has_billing_address** | **bool** | Indicates if billing address exists | [optional] 
**billing_addr1** | **str** | Billing address line 1 | [optional] 
**billing_addr2** | **str** | Billing address line 2 | [optional] 
**billing_city** | **str** | Billing address city | [optional] 
**billing_state** | **str** | Billing address state/province | [optional] 
**billing_zip** | **str** | Billing address postal/zip code | [optional] 
**billing_country** | **str** | Billing address country | [optional] 
**billing_phone1** | **str** | Billing department phone number | [optional] 
**billing_phone2** | **str** | Billing department alternate phone | [optional] 
**has_shipping_address** | **bool** | Indicates if shipping address exists | [optional] 
**shipping_addr1** | **str** | Shipping address line 1 | [optional] 
**shipping_addr2** | **str** | Shipping address line 2 | [optional] 
**shipping_city** | **str** | Shipping address city | [optional] 
**shipping_state** | **str** | Shipping address state/province | [optional] 
**shipping_zip** | **str** | Shipping address postal/zip code | [optional] 
**shipping_country** | **str** | Shipping address country | [optional] 
**customer_specific_requirements** | **str** | Customer specific delivery or service requirements | [optional] 
**notes** | **str** | General notes about the customer | [optional] 
**short_name** | **str** | Short name or alias for display purposes | [optional] 
**is_taxable** | **bool** | Indicates if customer is subject to tax | [optional] 
**tax_code** | **str** | Tax exemption code or tax ID | [optional] 
**opening_balance** | **float** | Opening account balance | [optional] 

## Example

```python
from openapi_client.models.customer_response import CustomerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerResponse from a JSON string
customer_response_instance = CustomerResponse.from_json(json)
# print the JSON string representation of the object
print(CustomerResponse.to_json())

# convert the object into a dict
customer_response_dict = customer_response_instance.to_dict()
# create an instance of CustomerResponse from a dict
customer_response_from_dict = CustomerResponse.from_dict(customer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


