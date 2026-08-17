# VariantAnnotations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bravo_af** | **float** |  | [optional] 
**gnomad_af_total** | **float** |  | [optional] 
**gnomad_af_afr** | **float** |  | [optional] 
**gnomad_af_afr_female** | **float** |  | [optional] 
**gnomad_af_afr_male** | **float** |  | [optional] 
**gnomad_af_ami** | **float** |  | [optional] 
**gnomad_af_ami_female** | **float** |  | [optional] 
**gnomad_af_ami_male** | **float** |  | [optional] 
**gnomad_af_amr** | **float** |  | [optional] 
**gnomad_af_amr_female** | **float** |  | [optional] 
**gnomad_af_amr_male** | **float** |  | [optional] 
**gnomad_af_asj** | **float** |  | [optional] 
**gnomad_af_asj_female** | **float** |  | [optional] 
**gnomad_af_asj_male** | **float** |  | [optional] 
**gnomad_af_eas** | **float** |  | [optional] 
**gnomad_af_eas_female** | **float** |  | [optional] 
**gnomad_af_eas_male** | **float** |  | [optional] 
**gnomad_af_female** | **float** |  | [optional] 
**gnomad_af_fin** | **float** |  | [optional] 
**gnomad_af_fin_female** | **float** |  | [optional] 
**gnomad_af_fin_male** | **float** |  | [optional] 
**gnomad_af_male** | **float** |  | [optional] 
**gnomad_af_nfe** | **float** |  | [optional] 
**gnomad_af_nfe_female** | **float** |  | [optional] 
**gnomad_af_nfe_male** | **float** |  | [optional] 
**gnomad_af_oth** | **float** |  | [optional] 
**gnomad_af_oth_female** | **float** |  | [optional] 
**gnomad_af_oth_male** | **float** |  | [optional] 
**gnomad_af_sas** | **float** |  | [optional] 
**gnomad_af_sas_male** | **float** |  | [optional] 
**gnomad_af_sas_female** | **float** |  | [optional] 
**gnomad_af_raw** | **float** |  | [optional] 
**gencode_category** | **str** |  | [optional] 
**funseq_description** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.variant_annotations import VariantAnnotations

# TODO update the JSON string below
json = "{}"
# create an instance of VariantAnnotations from a JSON string
variant_annotations_instance = VariantAnnotations.from_json(json)
# print the JSON string representation of the object
print(VariantAnnotations.to_json())

# convert the object into a dict
variant_annotations_dict = variant_annotations_instance.to_dict()
# create an instance of VariantAnnotations from a dict
variant_annotations_from_dict = VariantAnnotations.from_dict(variant_annotations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


