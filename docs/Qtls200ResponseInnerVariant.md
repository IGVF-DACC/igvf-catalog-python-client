# Qtls200ResponseInnerVariant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chr** | **str** |  | 
**pos** | **float** |  | 
**spdi** | **str** |  | [optional] 
**rsid** | [**ProteinsFromVariants200ResponseInnerProteinComplexAnyOf1ComplexAssembly**](ProteinsFromVariants200ResponseInnerProteinComplexAnyOf1ComplexAssembly.md) |  | [optional] 
**ca_id** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.qtls200_response_inner_variant import Qtls200ResponseInnerVariant

# TODO update the JSON string below
json = "{}"
# create an instance of Qtls200ResponseInnerVariant from a JSON string
qtls200_response_inner_variant_instance = Qtls200ResponseInnerVariant.from_json(json)
# print the JSON string representation of the object
print(Qtls200ResponseInnerVariant.to_json())

# convert the object into a dict
qtls200_response_inner_variant_dict = qtls200_response_inner_variant_instance.to_dict()
# create an instance of Qtls200ResponseInnerVariant from a dict
qtls200_response_inner_variant_from_dict = Qtls200ResponseInnerVariant.from_dict(qtls200_response_inner_variant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


