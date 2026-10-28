# PropertyScores


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** |  | 
**posterior_probability** | **float** |  | 
**p_value** | **float** |  | 
**affected_position** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.property_scores import PropertyScores

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyScores from a JSON string
property_scores_instance = PropertyScores.from_json(json)
# print the JSON string representation of the object
print(PropertyScores.to_json())

# convert the object into a dict
property_scores_dict = property_scores_instance.to_dict()
# create an instance of PropertyScores from a dict
property_scores_from_dict = PropertyScores.from_dict(property_scores_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


