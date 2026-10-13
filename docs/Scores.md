# Scores


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** |  | 
**score** | **float** |  | [optional] 
**source_url** | **str** |  | [optional] 
**files_filesets** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.scores import Scores

# TODO update the JSON string below
json = "{}"
# create an instance of Scores from a JSON string
scores_instance = Scores.from_json(json)
# print the JSON string representation of the object
print(Scores.to_json())

# convert the object into a dict
scores_dict = scores_instance.to_dict()
# create an instance of Scores from a dict
scores_from_dict = Scores.from_dict(scores_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


