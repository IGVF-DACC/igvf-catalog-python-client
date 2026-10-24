# GenesFromTranscriptsTranscript


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**transcript_type** | **str** |  | [optional] 
**chr** | **str** |  | [optional] 
**start** | **float** |  | [optional] 
**end** | **float** |  | [optional] 
**strand** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**gene_name** | **str** |  | [optional] 
**refseq_transcript_ids** | **List[str]** |  | [optional] 
**mane_select** | **bool** |  | [optional] 
**source** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**source_url** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.genes_from_transcripts_transcript import GenesFromTranscriptsTranscript

# TODO update the JSON string below
json = "{}"
# create an instance of GenesFromTranscriptsTranscript from a JSON string
genes_from_transcripts_transcript_instance = GenesFromTranscriptsTranscript.from_json(json)
# print the JSON string representation of the object
print(GenesFromTranscriptsTranscript.to_json())

# convert the object into a dict
genes_from_transcripts_transcript_dict = genes_from_transcripts_transcript_instance.to_dict()
# create an instance of GenesFromTranscriptsTranscript from a dict
genes_from_transcripts_transcript_from_dict = GenesFromTranscriptsTranscript.from_dict(genes_from_transcripts_transcript_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


