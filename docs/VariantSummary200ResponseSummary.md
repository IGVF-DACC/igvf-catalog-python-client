# VariantSummary200ResponseSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rsid** | **List[str]** |  | [optional] 
**varinfo** | **str** |  | [optional] 
**spdi** | **str** |  | [optional] 
**hgvs** | **str** |  | [optional] 
**ca_id** | **str** |  | [optional] 
**ref** | **str** |  | [optional] 
**alt** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.variant_summary200_response_summary import VariantSummary200ResponseSummary

# TODO update the JSON string below
json = "{}"
# create an instance of VariantSummary200ResponseSummary from a JSON string
variant_summary200_response_summary_instance = VariantSummary200ResponseSummary.from_json(json)
# print the JSON string representation of the object
print(VariantSummary200ResponseSummary.to_json())

# convert the object into a dict
variant_summary200_response_summary_dict = variant_summary200_response_summary_instance.to_dict()
# create an instance of VariantSummary200ResponseSummary from a dict
variant_summary200_response_summary_from_dict = VariantSummary200ResponseSummary.from_dict(variant_summary200_response_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


