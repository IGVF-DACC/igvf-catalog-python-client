# ProteinsFromVariants


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sequence_variant** | [**PhenotypesFromVariantsVariant**](PhenotypesFromVariantsVariant.md) |  | [optional] 
**protein_complex** | [**ProteinsFromVariantsProteinComplex**](ProteinsFromVariantsProteinComplex.md) |  | [optional] 
**biosample_term** | [**ProteinsFromVariantsBiosampleTerm**](ProteinsFromVariantsBiosampleTerm.md) |  | [optional] 
**biological_context** | **str** |  | [optional] 
**regulatory_type** | **str** |  | [optional] 
**var_class** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**name** | **str** |  | 
**method** | **str** |  | [optional] 
**files_filesets** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**source_url** | **str** |  | [optional] 
**is_complex** | **bool** |  | 
**score** | **float** |  | [optional] 
**neg_log10_pvalue_adj_ref** | **float** |  | [optional] 
**neg_log10_pvalue_adj_alt** | **float** |  | [optional] 
**motif** | **str** |  | [optional] 
**motif_log2_fc** | **float** |  | [optional] 
**beta** | **float** |  | [optional] 
**se** | **float** |  | [optional] 
**gene** | **str** |  | [optional] 
**gene_consequence** | **str** |  | [optional] 
**neg_log10_pvalue** | **float** |  | [optional] 
**p_value** | **float** |  | [optional] 
**neg_log10_pvalue_adj** | **float** |  | [optional] 
**variant_effect_score** | **float** |  | [optional] 
**se_mpl_annotation** | **str** |  | [optional] 
**se_mpl_baseline** | **float** |  | [optional] 
**alt_score** | **float** |  | [optional] 
**ref_score** | **float** |  | [optional] 
**relative_binding_affinity** | **float** |  | [optional] 
**effect_on_binding** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.proteins_from_variants import ProteinsFromVariants

# TODO update the JSON string below
json = "{}"
# create an instance of ProteinsFromVariants from a JSON string
proteins_from_variants_instance = ProteinsFromVariants.from_json(json)
# print the JSON string representation of the object
print(ProteinsFromVariants.to_json())

# convert the object into a dict
proteins_from_variants_dict = proteins_from_variants_instance.to_dict()
# create an instance of ProteinsFromVariants from a dict
proteins_from_variants_from_dict = ProteinsFromVariants.from_dict(proteins_from_variants_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


