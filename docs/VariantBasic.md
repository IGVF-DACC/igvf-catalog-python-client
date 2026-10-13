# VariantBasic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chr** | **str** |  | 
**pos** | **float** |  | 
**ref** | **str** |  | 
**alt** | **str** |  | 
**rsid** | **List[str]** |  | [optional] 
**spdi** | **str** |  | [optional] 
**hgvs** | **str** |  | [optional] 
**ca_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.variant_basic import VariantBasic

# TODO update the JSON string below
json = "{}"
# create an instance of VariantBasic from a JSON string
variant_basic_instance = VariantBasic.from_json(json)
# print the JSON string representation of the object
print(VariantBasic.to_json())

# convert the object into a dict
variant_basic_dict = variant_basic_instance.to_dict()
# create an instance of VariantBasic from a dict
variant_basic_from_dict = VariantBasic.from_dict(variant_basic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


