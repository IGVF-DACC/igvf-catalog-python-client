# PathwaysFromGenes200ResponseInner


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
**gene** | [**ProteinsFromGenes200ResponseInnerGene**](ProteinsFromGenes200ResponseInnerGene.md) |  | [optional] 
**pathway** | [**PathwaysFromGenes200ResponseInnerPathway**](PathwaysFromGenes200ResponseInnerPathway.md) |  | [optional] 
**name** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.pathways_from_genes200_response_inner import PathwaysFromGenes200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of PathwaysFromGenes200ResponseInner from a JSON string
pathways_from_genes200_response_inner_instance = PathwaysFromGenes200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(PathwaysFromGenes200ResponseInner.to_json())

# convert the object into a dict
pathways_from_genes200_response_inner_dict = pathways_from_genes200_response_inner_instance.to_dict()
# create an instance of PathwaysFromGenes200ResponseInner from a dict
pathways_from_genes200_response_inner_from_dict = PathwaysFromGenes200ResponseInner.from_dict(pathways_from_genes200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


