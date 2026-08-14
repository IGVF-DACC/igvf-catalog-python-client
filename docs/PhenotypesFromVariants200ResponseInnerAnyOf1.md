# PhenotypesFromVariants200ResponseInnerAnyOf1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**biological_context** | **str** |  | [optional] 
**source** | **str** |  | 
**source_url** | **str** |  | 
**score** | **float** |  | [optional] 
**effect_size** | **float** |  | [optional] 
**z_score** | **float** |  | [optional] 
**p_value** | **float** |  | [optional] 
**neg_log10_pvalue** | **float** |  | [optional] 
**significant** | **bool** |  | [optional] 
**num_guides** | **float** |  | [optional] 
**edit_rate_mean** | **float** |  | [optional] 
**effect_size_ci95_lower** | **float** |  | [optional] 
**effect_size_ci95_upper** | **float** |  | [optional] 
**crispr_modality** | **str** |  | [optional] 
**method** | **str** |  | 
**var_class** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**files_filesets** | **str** |  | 
**biosample_term** | **str** |  | [optional] 
**phenotype_term** | **str** |  | 
**variant** | [**ProteinsFromVariants200ResponseInnerSequenceVariant**](ProteinsFromVariants200ResponseInnerSequenceVariant.md) |  | 
**phenotype_id** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.phenotypes_from_variants200_response_inner_any_of1 import PhenotypesFromVariants200ResponseInnerAnyOf1

# TODO update the JSON string below
json = "{}"
# create an instance of PhenotypesFromVariants200ResponseInnerAnyOf1 from a JSON string
phenotypes_from_variants200_response_inner_any_of1_instance = PhenotypesFromVariants200ResponseInnerAnyOf1.from_json(json)
# print the JSON string representation of the object
print(PhenotypesFromVariants200ResponseInnerAnyOf1.to_json())

# convert the object into a dict
phenotypes_from_variants200_response_inner_any_of1_dict = phenotypes_from_variants200_response_inner_any_of1_instance.to_dict()
# create an instance of PhenotypesFromVariants200ResponseInnerAnyOf1 from a dict
phenotypes_from_variants200_response_inner_any_of1_from_dict = PhenotypesFromVariants200ResponseInnerAnyOf1.from_dict(phenotypes_from_variants200_response_inner_any_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


