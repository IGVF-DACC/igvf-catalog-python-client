# ProteinsFromGenes200ResponseInnerProtein


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
from igvf_catalog_client.models.proteins_from_genes200_response_inner_protein import ProteinsFromGenes200ResponseInnerProtein

# TODO update the JSON string below
json = "{}"
# create an instance of ProteinsFromGenes200ResponseInnerProtein from a JSON string
proteins_from_genes200_response_inner_protein_instance = ProteinsFromGenes200ResponseInnerProtein.from_json(json)
# print the JSON string representation of the object
print(ProteinsFromGenes200ResponseInnerProtein.to_json())

# convert the object into a dict
proteins_from_genes200_response_inner_protein_dict = proteins_from_genes200_response_inner_protein_instance.to_dict()
# create an instance of ProteinsFromGenes200ResponseInnerProtein from a dict
proteins_from_genes200_response_inner_protein_from_dict = ProteinsFromGenes200ResponseInnerProtein.from_dict(proteins_from_genes200_response_inner_protein_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


