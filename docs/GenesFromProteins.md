# GenesFromProteins


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gene** | [**DiseasesFromGenesGene**](DiseasesFromGenesGene.md) |  | [optional] 
**protein** | [**ComplexesFromProteinsProtein**](ComplexesFromProteinsProtein.md) |  | [optional] 

## Example

```python
from igvf_catalog_client.models.genes_from_proteins import GenesFromProteins

# TODO update the JSON string below
json = "{}"
# create an instance of GenesFromProteins from a JSON string
genes_from_proteins_instance = GenesFromProteins.from_json(json)
# print the JSON string representation of the object
print(GenesFromProteins.to_json())

# convert the object into a dict
genes_from_proteins_dict = genes_from_proteins_instance.to_dict()
# create an instance of GenesFromProteins from a dict
genes_from_proteins_from_dict = GenesFromProteins.from_dict(genes_from_proteins_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


