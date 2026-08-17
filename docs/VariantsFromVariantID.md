# VariantsFromVariantID


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
**sequence_variant** | [**VariantsFromVariantIDSequenceVariant**](VariantsFromVariantIDSequenceVariant.md) |  | [optional] 
**name** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.variants_from_variant_id import VariantsFromVariantID

# TODO update the JSON string below
json = "{}"
# create an instance of VariantsFromVariantID from a JSON string
variants_from_variant_id_instance = VariantsFromVariantID.from_json(json)
# print the JSON string representation of the object
print(VariantsFromVariantID.to_json())

# convert the object into a dict
variants_from_variant_id_dict = variants_from_variant_id_instance.to_dict()
# create an instance of VariantsFromVariantID from a dict
variants_from_variant_id_from_dict = VariantsFromVariantID.from_dict(variants_from_variant_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


