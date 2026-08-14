# TranscriptsFromGenes200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 
**source_url** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**gene** | [**ProteinsFromGenes200ResponseInnerGene**](ProteinsFromGenes200ResponseInnerGene.md) |  | [optional] 
**transcript** | [**TranscriptsFromGenes200ResponseInnerTranscript**](TranscriptsFromGenes200ResponseInnerTranscript.md) |  | [optional] 
**name** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.transcripts_from_genes200_response_inner import TranscriptsFromGenes200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of TranscriptsFromGenes200ResponseInner from a JSON string
transcripts_from_genes200_response_inner_instance = TranscriptsFromGenes200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(TranscriptsFromGenes200ResponseInner.to_json())

# convert the object into a dict
transcripts_from_genes200_response_inner_dict = transcripts_from_genes200_response_inner_instance.to_dict()
# create an instance of TranscriptsFromGenes200ResponseInner from a dict
transcripts_from_genes200_response_inner_from_dict = TranscriptsFromGenes200ResponseInner.from_dict(transcripts_from_genes200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


