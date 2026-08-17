# CodingVariant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**aapos** | **float** |  | [optional] 
**hgvsp** | **str** |  | [optional] 
**protein_name** | **str** |  | [optional] 
**gene_name** | **str** |  | [optional] 
**ref** | **str** |  | [optional] 
**alt** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.coding_variant import CodingVariant

# TODO update the JSON string below
json = "{}"
# create an instance of CodingVariant from a JSON string
coding_variant_instance = CodingVariant.from_json(json)
# print the JSON string representation of the object
print(CodingVariant.to_json())

# convert the object into a dict
coding_variant_dict = coding_variant_instance.to_dict()
# create an instance of CodingVariant from a dict
coding_variant_from_dict = CodingVariant.from_dict(coding_variant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


