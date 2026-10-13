# CodingVariantsSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variant_id** | **str** |  | [optional] 
**hgvsp** | **str** |  | [optional] 
**gene_name** | **str** |  | [optional] 
**transcript_id** | **str** |  | [optional] 
**data_type** | **str** |  | 
**score** | **float** |  | 
**portal_link** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.coding_variants_summary import CodingVariantsSummary

# TODO update the JSON string below
json = "{}"
# create an instance of CodingVariantsSummary from a JSON string
coding_variants_summary_instance = CodingVariantsSummary.from_json(json)
# print the JSON string representation of the object
print(CodingVariantsSummary.to_json())

# convert the object into a dict
coding_variants_summary_dict = coding_variants_summary_instance.to_dict()
# create an instance of CodingVariantsSummary from a dict
coding_variants_summary_from_dict = CodingVariantsSummary.from_dict(coding_variants_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


