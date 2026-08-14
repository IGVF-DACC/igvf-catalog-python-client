# VariantsFromDrugs200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sequence_variant** | [**BiosamplesFromVariants200ResponseInnerVariant**](BiosamplesFromVariants200ResponseInnerVariant.md) |  | [optional] 
**to** | **str** |  | 
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
from igvf_catalog_client.models.variants_from_drugs200_response_inner import VariantsFromDrugs200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of VariantsFromDrugs200ResponseInner from a JSON string
variants_from_drugs200_response_inner_instance = VariantsFromDrugs200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(VariantsFromDrugs200ResponseInner.to_json())

# convert the object into a dict
variants_from_drugs200_response_inner_dict = variants_from_drugs200_response_inner_instance.to_dict()
# create an instance of VariantsFromDrugs200ResponseInner from a dict
variants_from_drugs200_response_inner_from_dict = VariantsFromDrugs200ResponseInner.from_dict(variants_from_drugs200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


