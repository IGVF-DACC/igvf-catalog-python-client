# PhenotypesFromVariants200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rsid** | **List[str]** |  | [optional] 
**phenotype_id** | **str** |  | 
**phenotype_term** | **str** |  | 
**study** | [**PhenotypesFromVariants200ResponseInnerAnyOfStudy**](PhenotypesFromVariants200ResponseInnerAnyOfStudy.md) |  | [optional] 
**neg_log10_pvalue** | **float** |  | [optional] 
**p_value** | **float** |  | 
**beta** | **float** |  | 
**beta_ci_lower** | **float** |  | 
**beta_ci_upper** | **float** |  | 
**oddsr_ci_lower** | **float** |  | 
**oddsr_ci_upper** | **float** |  | 
**lead_chrom** | **str** |  | 
**lead_pos** | **float** |  | 
**lead_ref** | **str** |  | 
**lead_alt** | **str** |  | 
**direction** | **str** |  | 
**source** | **str** |  | 
**source_url** | **str** |  | 
**var_class** | **str** |  | [optional] 
**method** | **str** |  | 
**label** | **str** |  | [optional] 
**version** | **str** |  | [optional] [default to 'October 2022 (22.10)']
**name** | **str** |  | 
**variant** | [**ProteinsFromVariants200ResponseInnerSequenceVariant**](ProteinsFromVariants200ResponseInnerSequenceVariant.md) |  | 
**files_filesets** | **str** |  | 
**biological_context** | **str** |  | [optional] 
**score** | **float** |  | [optional] 
**effect_size** | **float** |  | [optional] 
**z_score** | **float** |  | [optional] 
**significant** | **bool** |  | [optional] 
**num_guides** | **float** |  | [optional] 
**edit_rate_mean** | **float** |  | [optional] 
**effect_size_ci95_lower** | **float** |  | [optional] 
**effect_size_ci95_upper** | **float** |  | [optional] 
**crispr_modality** | **str** |  | [optional] 
**biosample_term** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.phenotypes_from_variants200_response_inner import PhenotypesFromVariants200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of PhenotypesFromVariants200ResponseInner from a JSON string
phenotypes_from_variants200_response_inner_instance = PhenotypesFromVariants200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(PhenotypesFromVariants200ResponseInner.to_json())

# convert the object into a dict
phenotypes_from_variants200_response_inner_dict = phenotypes_from_variants200_response_inner_instance.to_dict()
# create an instance of PhenotypesFromVariants200ResponseInner from a dict
phenotypes_from_variants200_response_inner_from_dict = PhenotypesFromVariants200ResponseInner.from_dict(phenotypes_from_variants200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


