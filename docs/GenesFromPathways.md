# GenesFromPathways


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 
**source_url** | **str** |  | [optional] 
**orgnism** | **str** |  | [optional] 
**organism** | **str** |  | [optional] 
**var_class** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**files_filesets** | **str** |  | [optional] 
**gene** | [**DiseasesFromGenesGene**](DiseasesFromGenesGene.md) |  | [optional] 
**pathway** | [**GenesFromPathwaysPathway**](GenesFromPathwaysPathway.md) |  | [optional] 
**name** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.genes_from_pathways import GenesFromPathways

# TODO update the JSON string below
json = "{}"
# create an instance of GenesFromPathways from a JSON string
genes_from_pathways_instance = GenesFromPathways.from_json(json)
# print the JSON string representation of the object
print(GenesFromPathways.to_json())

# convert the object into a dict
genes_from_pathways_dict = genes_from_pathways_instance.to_dict()
# create an instance of GenesFromPathways from a dict
genes_from_pathways_from_dict = GenesFromPathways.from_dict(genes_from_pathways_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


