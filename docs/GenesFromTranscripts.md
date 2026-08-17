# GenesFromTranscripts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 
**source_url** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**gene** | [**DiseasesFromGenesGene**](DiseasesFromGenesGene.md) |  | [optional] 
**transcript** | [**GenesFromTranscriptsTranscript**](GenesFromTranscriptsTranscript.md) |  | [optional] 
**name** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.genes_from_transcripts import GenesFromTranscripts

# TODO update the JSON string below
json = "{}"
# create an instance of GenesFromTranscripts from a JSON string
genes_from_transcripts_instance = GenesFromTranscripts.from_json(json)
# print the JSON string representation of the object
print(GenesFromTranscripts.to_json())

# convert the object into a dict
genes_from_transcripts_dict = genes_from_transcripts_instance.to_dict()
# create an instance of GenesFromTranscripts from a dict
genes_from_transcripts_from_dict = GenesFromTranscripts.from_dict(genes_from_transcripts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


