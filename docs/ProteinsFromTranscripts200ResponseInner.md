# ProteinsFromTranscripts200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 
**source_url** | **str** |  | [optional] 
**protein** | [**ProteinsFromTranscripts200ResponseInnerProtein**](ProteinsFromTranscripts200ResponseInnerProtein.md) |  | [optional] 
**transcript** | [**TranscriptsFromGenes200ResponseInnerTranscript**](TranscriptsFromGenes200ResponseInnerTranscript.md) |  | [optional] 
**name** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.proteins_from_transcripts200_response_inner import ProteinsFromTranscripts200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProteinsFromTranscripts200ResponseInner from a JSON string
proteins_from_transcripts200_response_inner_instance = ProteinsFromTranscripts200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ProteinsFromTranscripts200ResponseInner.to_json())

# convert the object into a dict
proteins_from_transcripts200_response_inner_dict = proteins_from_transcripts200_response_inner_instance.to_dict()
# create an instance of ProteinsFromTranscripts200ResponseInner from a dict
proteins_from_transcripts200_response_inner_from_dict = ProteinsFromTranscripts200ResponseInner.from_dict(proteins_from_transcripts200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


