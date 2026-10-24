# PhenotypesFromVariants37


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
**p_value_adj** | **float** |  | [optional] 
**neg_log10_pvalue_adj** | **float** |  | [optional] 
**perturbation** | **str** |  | [optional] 
**protein_id** | **str** |  | [optional] 
**exon** | **str** |  | [optional] 
**target** | **str** |  | [optional] 
**consequence** | **str** |  | [optional] 
**standard_error** | **float** |  | [optional] 
**var_95_ci_upper** | **float** |  | [optional] 
**var_95_ci_lower** | **float** |  | [optional] 
**amino_acid_change** | **str** |  | [optional] 
**hgvs_p** | **str** |  | [optional] 
**functional_consequence** | **str** |  | [optional] 
**functional_consequence_zscore** | **float** |  | [optional] 
**variant_qc_flag** | **str** |  | [optional] 
**method** | **str** |  | 
**var_class** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**files_filesets** | **str** |  | 
**biosample_term** | **str** |  | [optional] 
**phenotype_term** | **str** |  | 
**variant** | [**PhenotypesFromVariantsVariant**](PhenotypesFromVariantsVariant.md) |  | 
**phenotype_id** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.phenotypes_from_variants37 import PhenotypesFromVariants37

# TODO update the JSON string below
json = "{}"
# create an instance of PhenotypesFromVariants37 from a JSON string
phenotypes_from_variants37_instance = PhenotypesFromVariants37.from_json(json)
# print the JSON string representation of the object
print(PhenotypesFromVariants37.to_json())

# convert the object into a dict
phenotypes_from_variants37_dict = phenotypes_from_variants37_instance.to_dict()
# create an instance of PhenotypesFromVariants37 from a dict
phenotypes_from_variants37_from_dict = PhenotypesFromVariants37.from_dict(phenotypes_from_variants37_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


