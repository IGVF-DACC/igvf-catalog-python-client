# StudyParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**study_parameter_id** | **str** |  | 
**study_type** | **str** |  | [optional] 
**study_cases** | **str** |  | [optional] 
**study_controls** | **str** |  | [optional] 
**p_value** | **str** |  | [optional] 
**biogeographical_groups** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.study_parameters import StudyParameters

# TODO update the JSON string below
json = "{}"
# create an instance of StudyParameters from a JSON string
study_parameters_instance = StudyParameters.from_json(json)
# print the JSON string representation of the object
print(StudyParameters.to_json())

# convert the object into a dict
study_parameters_dict = study_parameters_instance.to_dict()
# create an instance of StudyParameters from a dict
study_parameters_from_dict = StudyParameters.from_dict(study_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


