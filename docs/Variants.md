# Variants


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variant** | [**VariantBasic**](VariantBasic.md) |  | 
**scores** | [**List[Scores]**](Scores.md) |  | 

## Example

```python
from igvf_catalog_client.models.variants import Variants

# TODO update the JSON string below
json = "{}"
# create an instance of Variants from a JSON string
variants_instance = Variants.from_json(json)
# print the JSON string representation of the object
print(Variants.to_json())

# convert the object into a dict
variants_dict = variants_instance.to_dict()
# create an instance of Variants from a dict
variants_from_dict = Variants.from_dict(variants_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


