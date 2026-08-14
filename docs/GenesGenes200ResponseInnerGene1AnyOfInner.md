# GenesGenes200ResponseInnerGene1AnyOfInner


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

## Example

```python
from igvf_catalog_client.models.genes_genes200_response_inner_gene1_any_of_inner import GenesGenes200ResponseInnerGene1AnyOfInner

# TODO update the JSON string below
json = "{}"
# create an instance of GenesGenes200ResponseInnerGene1AnyOfInner from a JSON string
genes_genes200_response_inner_gene1_any_of_inner_instance = GenesGenes200ResponseInnerGene1AnyOfInner.from_json(json)
# print the JSON string representation of the object
print(GenesGenes200ResponseInnerGene1AnyOfInner.to_json())

# convert the object into a dict
genes_genes200_response_inner_gene1_any_of_inner_dict = genes_genes200_response_inner_gene1_any_of_inner_instance.to_dict()
# create an instance of GenesGenes200ResponseInnerGene1AnyOfInner from a dict
genes_genes200_response_inner_gene1_any_of_inner_from_dict = GenesGenes200ResponseInnerGene1AnyOfInner.from_dict(genes_genes200_response_inner_gene1_any_of_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


