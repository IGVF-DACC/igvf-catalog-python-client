# CaddScores


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raw** | **float** |  | [optional] 
**phread** | **float** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.cadd_scores import CaddScores

# TODO update the JSON string below
json = "{}"
# create an instance of CaddScores from a JSON string
cadd_scores_instance = CaddScores.from_json(json)
# print the JSON string representation of the object
print(CaddScores.to_json())

# convert the object into a dict
cadd_scores_dict = cadd_scores_instance.to_dict()
# create an instance of CaddScores from a dict
cadd_scores_from_dict = CaddScores.from_dict(cadd_scores_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


