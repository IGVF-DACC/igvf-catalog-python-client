# PathwaysFromPathways


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
**parent_pathway** | [**GenesFromPathwaysPathway**](GenesFromPathwaysPathway.md) |  | [optional] 
**child_pathway** | [**GenesFromPathwaysPathway**](GenesFromPathwaysPathway.md) |  | [optional] 
**name** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.pathways_from_pathways import PathwaysFromPathways

# TODO update the JSON string below
json = "{}"
# create an instance of PathwaysFromPathways from a JSON string
pathways_from_pathways_instance = PathwaysFromPathways.from_json(json)
# print the JSON string representation of the object
print(PathwaysFromPathways.to_json())

# convert the object into a dict
pathways_from_pathways_dict = pathways_from_pathways_instance.to_dict()
# create an instance of PathwaysFromPathways from a dict
pathways_from_pathways_from_dict = PathwaysFromPathways.from_dict(pathways_from_pathways_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


