# Qtls200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variant** | [**Qtls200ResponseInnerVariant**](Qtls200ResponseInnerVariant.md) |  | 
**gene** | [**Qtls200ResponseInnerGene**](Qtls200ResponseInnerGene.md) |  | 
**protein_complex** | [**Qtls200ResponseInnerGene**](Qtls200ResponseInnerGene.md) |  | 
**genomic_element** | [**Qtls200ResponseInnerGenomicElement**](Qtls200ResponseInnerGenomicElement.md) |  | 
**source** | **str** |  | 
**method** | **str** |  | 
**regulatory_type** | **str** |  | [optional] 
**gene_consequence** | **str** |  | [optional] 
**biological_context** | **str** |  | [optional] 
**neg_log10_pvalue** | **float** |  | [optional] 
**effect_size** | **float** |  | [optional] 
**posterior_inclusion_probability** | **float** |  | [optional] 
**intron_chr** | **str** |  | [optional] 
**intron_start** | [**VariantsAlleles200ResponseInnerInnerAnyOf**](VariantsAlleles200ResponseInnerInnerAnyOf.md) |  | [optional] 
**intron_end** | [**VariantsAlleles200ResponseInnerInnerAnyOf**](VariantsAlleles200ResponseInnerInnerAnyOf.md) |  | [optional] 
**study** | [**Qtls200ResponseInnerStudy**](Qtls200ResponseInnerStudy.md) |  | [optional] 
**files_filesets** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.qtls200_response_inner import Qtls200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of Qtls200ResponseInner from a JSON string
qtls200_response_inner_instance = Qtls200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(Qtls200ResponseInner.to_json())

# convert the object into a dict
qtls200_response_inner_dict = qtls200_response_inner_instance.to_dict()
# create an instance of Qtls200ResponseInner from a dict
qtls200_response_inner_from_dict = Qtls200ResponseInner.from_dict(qtls200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


