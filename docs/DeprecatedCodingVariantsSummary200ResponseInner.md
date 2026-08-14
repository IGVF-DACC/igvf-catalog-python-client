# DeprecatedCodingVariantsSummary200ResponseInner


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
from igvf_catalog_client.models.deprecated_coding_variants_summary200_response_inner import DeprecatedCodingVariantsSummary200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of DeprecatedCodingVariantsSummary200ResponseInner from a JSON string
deprecated_coding_variants_summary200_response_inner_instance = DeprecatedCodingVariantsSummary200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(DeprecatedCodingVariantsSummary200ResponseInner.to_json())

# convert the object into a dict
deprecated_coding_variants_summary200_response_inner_dict = deprecated_coding_variants_summary200_response_inner_instance.to_dict()
# create an instance of DeprecatedCodingVariantsSummary200ResponseInner from a dict
deprecated_coding_variants_summary200_response_inner_from_dict = DeprecatedCodingVariantsSummary200ResponseInner.from_dict(deprecated_coding_variants_summary200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


