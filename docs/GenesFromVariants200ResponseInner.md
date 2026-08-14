# GenesFromVariants200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gene** | [**GenesFromVariants200ResponseInnerGene**](GenesFromVariants200ResponseInnerGene.md) |  | 
**sequence_variant** | [**GenesFromVariants200ResponseInnerSequenceVariant**](GenesFromVariants200ResponseInnerSequenceVariant.md) |  | 
**intron_chr** | **str** |  | [optional] 
**intron_start** | **str** |  | [optional] 
**intron_end** | **str** |  | [optional] 
**effect_size** | **float** |  | [optional] 
**neg_log10_pvalue** | [**GenesFromVariants200ResponseInnerNegLog10Pvalue**](GenesFromVariants200ResponseInnerNegLog10Pvalue.md) |  | [optional] 
**neg_log10_pvalue_adj** | **float** |  | [optional] 
**log2_fc** | **float** |  | [optional] 
**posterior_inclusion_probability** | **float** |  | [optional] 
**coefficient_stddev** | **float** |  | [optional] 
**power** | **float** |  | [optional] 
**significant** | **bool** |  | [optional] 
**standard_error** | **float** |  | [optional] 
**z_score** | **float** |  | [optional] 
**credible_set_min_r2** | **float** |  | [optional] 
**method** | **str** |  | [optional] 
**crispr_modality** | **str** |  | [optional] 
**source** | **str** |  | 
**source_url** | **str** |  | 
**label** | **str** |  | 
**p_value** | **float** |  | [optional] 
**chr** | **str** |  | [optional] 
**biological_context** | **str** |  | 
**biosample_term** | **str** |  | 
**study** | [**GenesFromVariants200ResponseInnerStudy**](GenesFromVariants200ResponseInnerStudy.md) |  | [optional] 
**name** | **str** |  | [optional] 
**var_class** | **str** |  | [optional] 
**files_filesets** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.genes_from_variants200_response_inner import GenesFromVariants200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GenesFromVariants200ResponseInner from a JSON string
genes_from_variants200_response_inner_instance = GenesFromVariants200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GenesFromVariants200ResponseInner.to_json())

# convert the object into a dict
genes_from_variants200_response_inner_dict = genes_from_variants200_response_inner_instance.to_dict()
# create an instance of GenesFromVariants200ResponseInner from a dict
genes_from_variants200_response_inner_from_dict = GenesFromVariants200ResponseInner.from_dict(genes_from_variants200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


