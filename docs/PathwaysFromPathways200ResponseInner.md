# PathwaysFromPathways200ResponseInner


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
**parent_pathway** | [**PathwaysFromGenes200ResponseInnerPathway**](PathwaysFromGenes200ResponseInnerPathway.md) |  | [optional] 
**child_pathway** | [**PathwaysFromGenes200ResponseInnerPathway**](PathwaysFromGenes200ResponseInnerPathway.md) |  | [optional] 
**name** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.pathways_from_pathways200_response_inner import PathwaysFromPathways200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of PathwaysFromPathways200ResponseInner from a JSON string
pathways_from_pathways200_response_inner_instance = PathwaysFromPathways200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(PathwaysFromPathways200ResponseInner.to_json())

# convert the object into a dict
pathways_from_pathways200_response_inner_dict = pathways_from_pathways200_response_inner_instance.to_dict()
# create an instance of PathwaysFromPathways200ResponseInner from a dict
pathways_from_pathways200_response_inner_from_dict = PathwaysFromPathways200ResponseInner.from_dict(pathways_from_pathways200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


