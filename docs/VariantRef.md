# VariantRef


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

## Example

```python
from igvf_catalog_client.models.variant_ref import VariantRef

# TODO update the JSON string below
json = "{}"
# create an instance of VariantRef from a JSON string
variant_ref_instance = VariantRef.from_json(json)
# print the JSON string representation of the object
print(VariantRef.to_json())

# convert the object into a dict
variant_ref_dict = variant_ref_instance.to_dict()
# create an instance of VariantRef from a dict
variant_ref_from_dict = VariantRef.from_dict(variant_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


