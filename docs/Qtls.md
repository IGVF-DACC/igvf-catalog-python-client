# Qtls


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variant** | [**Variant**](Variant.md) |  | 
**gene** | [**IdName**](IdName.md) |  | 
**protein_complex** | [**IdName**](IdName.md) |  | 
**genomic_element** | [**GenomicElement5**](GenomicElement5.md) |  | 
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
**study** | [**Study2**](Study2.md) |  | [optional] 
**files_filesets** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.qtls import Qtls

# TODO update the JSON string below
json = "{}"
# create an instance of Qtls from a JSON string
qtls_instance = Qtls.from_json(json)
# print the JSON string representation of the object
print(Qtls.to_json())

# convert the object into a dict
qtls_dict = qtls_instance.to_dict()
# create an instance of Qtls from a dict
qtls_from_dict = Qtls.from_dict(qtls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


