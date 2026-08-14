# CodingVariantsFromGenes200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protein_change** | [**CodingVariantsFromGenes200ResponseInnerProteinChange**](CodingVariantsFromGenes200ResponseInnerProteinChange.md) |  | 
**variants** | [**List[CodingVariantsFromGenes200ResponseInnerVariantsInner]**](CodingVariantsFromGenes200ResponseInnerVariantsInner.md) |  | [optional] 

## Example

```python
from igvf_catalog_client.models.coding_variants_from_genes200_response_inner import CodingVariantsFromGenes200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of CodingVariantsFromGenes200ResponseInner from a JSON string
coding_variants_from_genes200_response_inner_instance = CodingVariantsFromGenes200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(CodingVariantsFromGenes200ResponseInner.to_json())

# convert the object into a dict
coding_variants_from_genes200_response_inner_dict = coding_variants_from_genes200_response_inner_instance.to_dict()
# create an instance of CodingVariantsFromGenes200ResponseInner from a dict
coding_variants_from_genes200_response_inner_from_dict = CodingVariantsFromGenes200ResponseInner.from_dict(coding_variants_from_genes200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


