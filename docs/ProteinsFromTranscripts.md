# ProteinsFromTranscripts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 
**source_url** | **str** |  | [optional] 
**protein** | [**ProteinsFromTranscriptsProtein**](ProteinsFromTranscriptsProtein.md) |  | [optional] 
**transcript** | [**GenesFromTranscriptsTranscript**](GenesFromTranscriptsTranscript.md) |  | [optional] 
**name** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.proteins_from_transcripts import ProteinsFromTranscripts

# TODO update the JSON string below
json = "{}"
# create an instance of ProteinsFromTranscripts from a JSON string
proteins_from_transcripts_instance = ProteinsFromTranscripts.from_json(json)
# print the JSON string representation of the object
print(ProteinsFromTranscripts.to_json())

# convert the object into a dict
proteins_from_transcripts_dict = proteins_from_transcripts_instance.to_dict()
# create an instance of ProteinsFromTranscripts from a dict
proteins_from_transcripts_from_dict = ProteinsFromTranscripts.from_dict(proteins_from_transcripts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


