# GenesFromVariants200ResponseInnerGeneAnyOf


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
from igvf_catalog_client.models.genes_from_variants200_response_inner_gene_any_of import GenesFromVariants200ResponseInnerGeneAnyOf

# TODO update the JSON string below
json = "{}"
# create an instance of GenesFromVariants200ResponseInnerGeneAnyOf from a JSON string
genes_from_variants200_response_inner_gene_any_of_instance = GenesFromVariants200ResponseInnerGeneAnyOf.from_json(json)
# print the JSON string representation of the object
print(GenesFromVariants200ResponseInnerGeneAnyOf.to_json())

# convert the object into a dict
genes_from_variants200_response_inner_gene_any_of_dict = genes_from_variants200_response_inner_gene_any_of_instance.to_dict()
# create an instance of GenesFromVariants200ResponseInnerGeneAnyOf from a dict
genes_from_variants200_response_inner_gene_any_of_from_dict = GenesFromVariants200ResponseInnerGeneAnyOf.from_dict(genes_from_variants200_response_inner_gene_any_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


