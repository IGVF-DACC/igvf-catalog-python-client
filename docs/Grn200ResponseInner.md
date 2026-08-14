# Grn200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_gene** | **str** |  | 
**genomic_element** | [**Grn200ResponseInnerGenomicElement**](Grn200ResponseInnerGenomicElement.md) |  | 
**crispr_modality** | **str** |  | [optional] 
**var_class** | **str** |  | 
**method** | **str** |  | 
**source** | **str** |  | 
**biological_context** | **str** |  | 
**files_filesets** | **str** |  | 
**log2_fc** | **float** |  | [optional] 
**neg_log10_pvalue** | [**GenesFromVariants200ResponseInnerNegLog10Pvalue**](GenesFromVariants200ResponseInnerNegLog10Pvalue.md) |  | [optional] 
**neg_log10_pvalue_adj** | [**GenesFromVariants200ResponseInnerNegLog10Pvalue**](GenesFromVariants200ResponseInnerNegLog10Pvalue.md) |  | [optional] 
**significant** | **bool** |  | [optional] 
**perturbation_efficiency_log2_fc** | **float** |  | [optional] 
**perturbation_efficiency_neg_log10_pvalue** | [**GenesFromVariants200ResponseInnerNegLog10Pvalue**](GenesFromVariants200ResponseInnerNegLog10Pvalue.md) |  | [optional] 
**perturbation_efficiency_neg_log10_pvalue_adj** | [**GenesFromVariants200ResponseInnerNegLog10Pvalue**](GenesFromVariants200ResponseInnerNegLog10Pvalue.md) |  | [optional] 
**perturbation_efficiency_significant** | **bool** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.grn200_response_inner import Grn200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of Grn200ResponseInner from a JSON string
grn200_response_inner_instance = Grn200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(Grn200ResponseInner.to_json())

# convert the object into a dict
grn200_response_inner_dict = grn200_response_inner_instance.to_dict()
# create an instance of Grn200ResponseInner from a dict
grn200_response_inner_from_dict = Grn200ResponseInner.from_dict(grn200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


