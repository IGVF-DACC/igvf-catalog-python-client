# PhenotypesFromVariants


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
**source_url** | **str** |  | [optional] 
**var_class** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**version** | **str** |  | [optional] [default to 'October 2022 (22.10)']
**name** | **str** |  | 
**variant** | [**PhenotypesFromVariantsVariant**](PhenotypesFromVariantsVariant.md) |  | 
**files_filesets** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.phenotypes_from_variants import PhenotypesFromVariants

# TODO update the JSON string below
json = "{}"
# create an instance of PhenotypesFromVariants from a JSON string
phenotypes_from_variants_instance = PhenotypesFromVariants.from_json(json)
# print the JSON string representation of the object
print(PhenotypesFromVariants.to_json())

# convert the object into a dict
phenotypes_from_variants_dict = phenotypes_from_variants_instance.to_dict()
# create an instance of PhenotypesFromVariants from a dict
phenotypes_from_variants_from_dict = PhenotypesFromVariants.from_dict(phenotypes_from_variants_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


