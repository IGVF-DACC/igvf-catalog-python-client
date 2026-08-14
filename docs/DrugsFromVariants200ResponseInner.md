# DrugsFromVariants200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drug** | [**DrugsFromVariants200ResponseInnerDrug**](DrugsFromVariants200ResponseInnerDrug.md) |  | [optional] 
**var_from** | **str** |  | 
**gene_symbol** | **List[str]** |  | [optional] 
**pmid** | **str** |  | [optional] 
**study_parameters** | [**List[DrugsFromVariants200ResponseInnerStudyParametersInner]**](DrugsFromVariants200ResponseInnerStudyParametersInner.md) |  | [optional] 
**phenotype_categories** | **List[str]** |  | [optional] 
**source** | **str** |  | 
**source_url** | **str** |  | 
**name** | **str** |  | 
**var_class** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**files_filesets** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.drugs_from_variants200_response_inner import DrugsFromVariants200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of DrugsFromVariants200ResponseInner from a JSON string
drugs_from_variants200_response_inner_instance = DrugsFromVariants200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(DrugsFromVariants200ResponseInner.to_json())

# convert the object into a dict
drugs_from_variants200_response_inner_dict = drugs_from_variants200_response_inner_instance.to_dict()
# create an instance of DrugsFromVariants200ResponseInner from a dict
drugs_from_variants200_response_inner_from_dict = DrugsFromVariants200ResponseInner.from_dict(drugs_from_variants200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


