# VariantsFromPhenotypesItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rsid** | **List[str]** |  | [optional] 
**phenotype_id** | **str** |  | 
**phenotype_term** | **str** |  | 
**study** | [**PhenotypesFromVariantsStudy**](PhenotypesFromVariantsStudy.md) |  | [optional] 
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
**variant** | [**PhenotypesFromVariantsVariant**](PhenotypesFromVariantsVariant.md) |  | 
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
from igvf_catalog_client.models.variants_from_phenotypes_item import VariantsFromPhenotypesItem

# TODO update the JSON string below
json = "{}"
# create an instance of VariantsFromPhenotypesItem from a JSON string
variants_from_phenotypes_item_instance = VariantsFromPhenotypesItem.from_json(json)
# print the JSON string representation of the object
print(VariantsFromPhenotypesItem.to_json())

# convert the object into a dict
variants_from_phenotypes_item_dict = variants_from_phenotypes_item_instance.to_dict()
# create an instance of VariantsFromPhenotypesItem from a dict
variants_from_phenotypes_item_from_dict = VariantsFromPhenotypesItem.from_dict(variants_from_phenotypes_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


