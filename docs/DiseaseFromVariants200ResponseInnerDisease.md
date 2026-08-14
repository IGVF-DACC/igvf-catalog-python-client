# DiseaseFromVariants200ResponseInnerDisease


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** |  | 
**term_id** | **str** |  | 
**name** | **str** |  | 
**synonyms** | **List[str]** |  | [optional] 
**description** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**subontology** | **str** |  | [optional] 
**source_url** | **str** |  | [optional] 
**var_class** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**files_filesets** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.disease_from_variants200_response_inner_disease import DiseaseFromVariants200ResponseInnerDisease

# TODO update the JSON string below
json = "{}"
# create an instance of DiseaseFromVariants200ResponseInnerDisease from a JSON string
disease_from_variants200_response_inner_disease_instance = DiseaseFromVariants200ResponseInnerDisease.from_json(json)
# print the JSON string representation of the object
print(DiseaseFromVariants200ResponseInnerDisease.to_json())

# convert the object into a dict
disease_from_variants200_response_inner_disease_dict = disease_from_variants200_response_inner_disease_instance.to_dict()
# create an instance of DiseaseFromVariants200ResponseInnerDisease from a dict
disease_from_variants200_response_inner_disease_from_dict = DiseaseFromVariants200ResponseInnerDisease.from_dict(disease_from_variants200_response_inner_disease_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


