# GenesFromTranscriptsTranscript


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


