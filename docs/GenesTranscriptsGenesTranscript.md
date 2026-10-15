# GenesTranscriptsGenesTranscript


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
**refseq_transcript_ids** | **List[str]** |  | [optional] 
**mane_select** | **bool** |  | [optional] 
**source** | **str** |  | 
**version** | **str** |  | 
**source_url** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.genes_transcripts_genes_transcript import GenesTranscriptsGenesTranscript

# TODO update the JSON string below
json = "{}"
# create an instance of GenesTranscriptsGenesTranscript from a JSON string
genes_transcripts_genes_transcript_instance = GenesTranscriptsGenesTranscript.from_json(json)
# print the JSON string representation of the object
print(GenesTranscriptsGenesTranscript.to_json())

# convert the object into a dict
genes_transcripts_genes_transcript_dict = genes_transcripts_genes_transcript_instance.to_dict()
# create an instance of GenesTranscriptsGenesTranscript from a dict
genes_transcripts_genes_transcript_from_dict = GenesTranscriptsGenesTranscript.from_dict(genes_transcripts_genes_transcript_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


