# TranscriptsFromGenes200ResponseInnerTranscript


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**transcript_type** | **str** |  | 
**chr** | **str** |  | 
**start** | **float** |  | 
**end** | **float** |  | 
**strand** | **str** |  | 
**name** | **str** |  | 
**gene_name** | **str** |  | 
**mane_select** | **bool** |  | [optional] 
**source** | **str** |  | 
**version** | **str** |  | 
**source_url** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.transcripts_from_genes200_response_inner_transcript import TranscriptsFromGenes200ResponseInnerTranscript

# TODO update the JSON string below
json = "{}"
# create an instance of TranscriptsFromGenes200ResponseInnerTranscript from a JSON string
transcripts_from_genes200_response_inner_transcript_instance = TranscriptsFromGenes200ResponseInnerTranscript.from_json(json)
# print the JSON string representation of the object
print(TranscriptsFromGenes200ResponseInnerTranscript.to_json())

# convert the object into a dict
transcripts_from_genes200_response_inner_transcript_dict = transcripts_from_genes200_response_inner_transcript_instance.to_dict()
# create an instance of TranscriptsFromGenes200ResponseInnerTranscript from a dict
transcripts_from_genes200_response_inner_transcript_from_dict = TranscriptsFromGenes200ResponseInnerTranscript.from_dict(transcripts_from_genes200_response_inner_transcript_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


