# ProteinsFromGenes200ResponseInnerProteinAnyOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | [optional] 
**uniprot_names** | **List[str]** |  | [optional] 
**uniprot_full_names** | **List[str]** |  | [optional] 
**uniprot_ids** | **List[str]** |  | [optional] 
**dbxrefs** | [**List[ProteinsFromGenes200ResponseInnerProteinAnyOfDbxrefsInner]**](ProteinsFromGenes200ResponseInnerProteinAnyOfDbxrefsInner.md) |  | [optional] 
**mane_select** | **bool** |  | [optional] 
**organism** | **str** |  | 
**source** | **str** |  | 
**source_url** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.proteins_from_genes200_response_inner_protein_any_of import ProteinsFromGenes200ResponseInnerProteinAnyOf

# TODO update the JSON string below
json = "{}"
# create an instance of ProteinsFromGenes200ResponseInnerProteinAnyOf from a JSON string
proteins_from_genes200_response_inner_protein_any_of_instance = ProteinsFromGenes200ResponseInnerProteinAnyOf.from_json(json)
# print the JSON string representation of the object
print(ProteinsFromGenes200ResponseInnerProteinAnyOf.to_json())

# convert the object into a dict
proteins_from_genes200_response_inner_protein_any_of_dict = proteins_from_genes200_response_inner_protein_any_of_instance.to_dict()
# create an instance of ProteinsFromGenes200ResponseInnerProteinAnyOf from a dict
proteins_from_genes200_response_inner_protein_any_of_from_dict = ProteinsFromGenes200ResponseInnerProteinAnyOf.from_dict(proteins_from_genes200_response_inner_protein_any_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


