# ProteinsFromGenes200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gene** | [**ProteinsFromGenes200ResponseInnerGene**](ProteinsFromGenes200ResponseInnerGene.md) |  | [optional] 
**protein** | [**ProteinsFromGenes200ResponseInnerProtein**](ProteinsFromGenes200ResponseInnerProtein.md) |  | [optional] 

## Example

```python
from igvf_catalog_client.models.proteins_from_genes200_response_inner import ProteinsFromGenes200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProteinsFromGenes200ResponseInner from a JSON string
proteins_from_genes200_response_inner_instance = ProteinsFromGenes200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ProteinsFromGenes200ResponseInner.to_json())

# convert the object into a dict
proteins_from_genes200_response_inner_dict = proteins_from_genes200_response_inner_instance.to_dict()
# create an instance of ProteinsFromGenes200ResponseInner from a dict
proteins_from_genes200_response_inner_from_dict = ProteinsFromGenes200ResponseInner.from_dict(proteins_from_genes200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


