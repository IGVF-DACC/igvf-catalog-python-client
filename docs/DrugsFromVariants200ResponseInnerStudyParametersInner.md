# DrugsFromVariants200ResponseInnerStudyParametersInner


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
from igvf_catalog_client.models.drugs_from_variants200_response_inner_study_parameters_inner import DrugsFromVariants200ResponseInnerStudyParametersInner

# TODO update the JSON string below
json = "{}"
# create an instance of DrugsFromVariants200ResponseInnerStudyParametersInner from a JSON string
drugs_from_variants200_response_inner_study_parameters_inner_instance = DrugsFromVariants200ResponseInnerStudyParametersInner.from_json(json)
# print the JSON string representation of the object
print(DrugsFromVariants200ResponseInnerStudyParametersInner.to_json())

# convert the object into a dict
drugs_from_variants200_response_inner_study_parameters_inner_dict = drugs_from_variants200_response_inner_study_parameters_inner_instance.to_dict()
# create an instance of DrugsFromVariants200ResponseInnerStudyParametersInner from a dict
drugs_from_variants200_response_inner_study_parameters_inner_from_dict = DrugsFromVariants200ResponseInnerStudyParametersInner.from_dict(drugs_from_variants200_response_inner_study_parameters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


