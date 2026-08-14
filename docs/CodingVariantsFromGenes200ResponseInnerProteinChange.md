# CodingVariantsFromGenes200ResponseInnerProteinChange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protein_id** | **str** |  | [optional] 
**protein_name** | **str** |  | [optional] 
**transcript_id** | **str** |  | [optional] 
**hgvsp** | **str** |  | [optional] 
**aapos** | **float** |  | [optional] 
**ref** | **str** |  | [optional] 
**alt** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.coding_variants_from_genes200_response_inner_protein_change import CodingVariantsFromGenes200ResponseInnerProteinChange

# TODO update the JSON string below
json = "{}"
# create an instance of CodingVariantsFromGenes200ResponseInnerProteinChange from a JSON string
coding_variants_from_genes200_response_inner_protein_change_instance = CodingVariantsFromGenes200ResponseInnerProteinChange.from_json(json)
# print the JSON string representation of the object
print(CodingVariantsFromGenes200ResponseInnerProteinChange.to_json())

# convert the object into a dict
coding_variants_from_genes200_response_inner_protein_change_dict = coding_variants_from_genes200_response_inner_protein_change_instance.to_dict()
# create an instance of CodingVariantsFromGenes200ResponseInnerProteinChange from a dict
coding_variants_from_genes200_response_inner_protein_change_from_dict = CodingVariantsFromGenes200ResponseInnerProteinChange.from_dict(coding_variants_from_genes200_response_inner_protein_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


