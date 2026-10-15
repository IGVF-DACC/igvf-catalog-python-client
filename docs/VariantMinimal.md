# VariantMinimal


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

## Example

```python
from igvf_catalog_client.models.variant_minimal import VariantMinimal

# TODO update the JSON string below
json = "{}"
# create an instance of VariantMinimal from a JSON string
variant_minimal_instance = VariantMinimal.from_json(json)
# print the JSON string representation of the object
print(VariantMinimal.to_json())

# convert the object into a dict
variant_minimal_dict = variant_minimal_instance.to_dict()
# create an instance of VariantMinimal from a dict
variant_minimal_from_dict = VariantMinimal.from_dict(variant_minimal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


