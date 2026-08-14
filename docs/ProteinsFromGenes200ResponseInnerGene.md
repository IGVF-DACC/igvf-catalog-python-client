# ProteinsFromGenes200ResponseInnerGene


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**chr** | **str** |  | 
**start** | **float** |  | 
**end** | **float** |  | 
**gene_type** | **str** |  | 
**name** | **str** |  | 
**strand** | **str** |  | [optional] 
**hgnc** | **str** |  | [optional] 
**entrez** | **str** |  | [optional] 
**collections** | **List[str]** |  | [optional] 
**study_sets** | **List[str]** |  | [optional] 
**source** | **str** |  | 
**version** | **str** |  | 
**source_url** | **str** |  | 
**synonyms** | **List[str]** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.proteins_from_genes200_response_inner_gene import ProteinsFromGenes200ResponseInnerGene

# TODO update the JSON string below
json = "{}"
# create an instance of ProteinsFromGenes200ResponseInnerGene from a JSON string
proteins_from_genes200_response_inner_gene_instance = ProteinsFromGenes200ResponseInnerGene.from_json(json)
# print the JSON string representation of the object
print(ProteinsFromGenes200ResponseInnerGene.to_json())

# convert the object into a dict
proteins_from_genes200_response_inner_gene_dict = proteins_from_genes200_response_inner_gene_instance.to_dict()
# create an instance of ProteinsFromGenes200ResponseInnerGene from a dict
proteins_from_genes200_response_inner_gene_from_dict = ProteinsFromGenes200ResponseInnerGene.from_dict(proteins_from_genes200_response_inner_gene_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


