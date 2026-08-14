# GenesGenes200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**gene_1** | [**GenesGenes200ResponseInnerGene1**](GenesGenes200ResponseInnerGene1.md) |  | 
**gene_2** | [**GenesGenes200ResponseInnerGene1**](GenesGenes200ResponseInnerGene1.md) |  | 
**z_score** | **float** |  | [optional] 
**associated_process** | **str** |  | [optional] 
**detection_method** | **str** |  | [optional] 
**detection_method_code** | **str** |  | [optional] 
**interaction_type** | **List[str]** |  | [optional] 
**interaction_type_code** | **List[str]** |  | [optional] 
**confidence_value_biogrid** | **float** |  | [optional] 
**confidence_value_intact** | **float** |  | [optional] 
**pmids** | **List[str]** |  | [optional] 
**label** | **str** |  | 
**method** | **str** |  | 
**var_class** | **str** |  | 
**source** | **str** |  | 
**source_url** | **str** |  | [optional] 
**name** | **str** |  | 
**files_filesets** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.genes_genes200_response_inner import GenesGenes200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GenesGenes200ResponseInner from a JSON string
genes_genes200_response_inner_instance = GenesGenes200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GenesGenes200ResponseInner.to_json())

# convert the object into a dict
genes_genes200_response_inner_dict = genes_genes200_response_inner_instance.to_dict()
# create an instance of GenesGenes200ResponseInner from a dict
genes_genes200_response_inner_from_dict = GenesGenes200ResponseInner.from_dict(genes_genes200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


