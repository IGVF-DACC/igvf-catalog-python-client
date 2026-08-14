# VariantsFromVariantID200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chr** | **str** |  | 
**ancestry** | **str** |  | 
**d_prime** | **float** |  | 
**r2** | **float** |  | 
**label** | **str** |  | 
**variant_1_base_pair** | **str** |  | 
**variant_1_rsid** | **str** |  | 
**variant_2_base_pair** | **str** |  | 
**variant_2_rsid** | **str** |  | 
**variant_1_pos** | **float** |  | [optional] 
**variant_1_spdi** | **str** |  | [optional] 
**variant_1_hgvs** | **str** |  | [optional] 
**variant_2_pos** | **float** |  | [optional] 
**variant_2_spdi** | **str** |  | [optional] 
**variant_2_hgvs** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**source_url** | **str** |  | [optional] 
**sequence_variant** | [**VariantsFromVariantID200ResponseInnerSequenceVariant**](VariantsFromVariantID200ResponseInnerSequenceVariant.md) |  | [optional] 
**name** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.variants_from_variant_id200_response_inner import VariantsFromVariantID200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of VariantsFromVariantID200ResponseInner from a JSON string
variants_from_variant_id200_response_inner_instance = VariantsFromVariantID200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(VariantsFromVariantID200ResponseInner.to_json())

# convert the object into a dict
variants_from_variant_id200_response_inner_dict = variants_from_variant_id200_response_inner_instance.to_dict()
# create an instance of VariantsFromVariantID200ResponseInner from a dict
variants_from_variant_id200_response_inner_from_dict = VariantsFromVariantID200ResponseInner.from_dict(variants_from_variant_id200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


