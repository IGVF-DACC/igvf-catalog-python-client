# GenesProteinsGenesProteins


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protein** | [**ProteinCompact**](ProteinCompact.md) |  | [optional] 
**gene** | [**GeneCompact**](GeneCompact.md) |  | [optional] 
**related** | [**List[RelatedItem]**](RelatedItem.md) |  | [optional] 

## Example

```python
from igvf_catalog_client.models.genes_proteins_genes_proteins import GenesProteinsGenesProteins

# TODO update the JSON string below
json = "{}"
# create an instance of GenesProteinsGenesProteins from a JSON string
genes_proteins_genes_proteins_instance = GenesProteinsGenesProteins.from_json(json)
# print the JSON string representation of the object
print(GenesProteinsGenesProteins.to_json())

# convert the object into a dict
genes_proteins_genes_proteins_dict = genes_proteins_genes_proteins_instance.to_dict()
# create an instance of GenesProteinsGenesProteins from a dict
genes_proteins_genes_proteins_from_dict = GenesProteinsGenesProteins.from_dict(genes_proteins_genes_proteins_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


