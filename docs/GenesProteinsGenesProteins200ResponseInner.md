# GenesProteinsGenesProteins200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protein** | [**GenesProteinsFromVariants200ResponseInnerRelatedInnerProtein**](GenesProteinsFromVariants200ResponseInnerRelatedInnerProtein.md) |  | [optional] 
**gene** | [**GenesProteinsFromVariants200ResponseInnerRelatedInnerGeneAnyOf**](GenesProteinsFromVariants200ResponseInnerRelatedInnerGeneAnyOf.md) |  | [optional] 
**related** | [**List[GenesProteinsGenesProteins200ResponseInnerRelatedInner]**](GenesProteinsGenesProteins200ResponseInnerRelatedInner.md) |  | [optional] 

## Example

```python
from igvf_catalog_client.models.genes_proteins_genes_proteins200_response_inner import GenesProteinsGenesProteins200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GenesProteinsGenesProteins200ResponseInner from a JSON string
genes_proteins_genes_proteins200_response_inner_instance = GenesProteinsGenesProteins200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GenesProteinsGenesProteins200ResponseInner.to_json())

# convert the object into a dict
genes_proteins_genes_proteins200_response_inner_dict = genes_proteins_genes_proteins200_response_inner_instance.to_dict()
# create an instance of GenesProteinsGenesProteins200ResponseInner from a dict
genes_proteins_genes_proteins200_response_inner_from_dict = GenesProteinsGenesProteins200ResponseInner.from_dict(genes_proteins_genes_proteins200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


