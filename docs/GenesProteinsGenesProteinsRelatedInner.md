# GenesProteinsGenesProteinsRelatedInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**uniprot_names** | **List[str]** |  | 
**files_filesets** | **str** |  | [optional] 
**chr** | **str** |  | 
**gene_id** | **str** |  | 
**hgnc** | **str** |  | [optional] 
**organism** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.genes_proteins_genes_proteins_related_inner import GenesProteinsGenesProteinsRelatedInner

# TODO update the JSON string below
json = "{}"
# create an instance of GenesProteinsGenesProteinsRelatedInner from a JSON string
genes_proteins_genes_proteins_related_inner_instance = GenesProteinsGenesProteinsRelatedInner.from_json(json)
# print the JSON string representation of the object
print(GenesProteinsGenesProteinsRelatedInner.to_json())

# convert the object into a dict
genes_proteins_genes_proteins_related_inner_dict = genes_proteins_genes_proteins_related_inner_instance.to_dict()
# create an instance of GenesProteinsGenesProteinsRelatedInner from a dict
genes_proteins_genes_proteins_related_inner_from_dict = GenesProteinsGenesProteinsRelatedInner.from_dict(genes_proteins_genes_proteins_related_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


