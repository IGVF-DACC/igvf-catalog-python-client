# VariantsFromVariantIDSummary200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ancestry** | **str** |  | 
**d_prime** | **float** |  | [optional] 
**r2** | **float** |  | [optional] 
**sequence_variant** | [**ProteinsFromVariants200ResponseInnerSequenceVariant**](ProteinsFromVariants200ResponseInnerSequenceVariant.md) |  | 
**predictions** | [**VariantsFromVariantIDSummary200ResponseInnerPredictions**](VariantsFromVariantIDSummary200ResponseInnerPredictions.md) |  | 

## Example

```python
from igvf_catalog_client.models.variants_from_variant_id_summary200_response_inner import VariantsFromVariantIDSummary200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of VariantsFromVariantIDSummary200ResponseInner from a JSON string
variants_from_variant_id_summary200_response_inner_instance = VariantsFromVariantIDSummary200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(VariantsFromVariantIDSummary200ResponseInner.to_json())

# convert the object into a dict
variants_from_variant_id_summary200_response_inner_dict = variants_from_variant_id_summary200_response_inner_instance.to_dict()
# create an instance of VariantsFromVariantIDSummary200ResponseInner from a dict
variants_from_variant_id_summary200_response_inner_from_dict = VariantsFromVariantIDSummary200ResponseInner.from_dict(variants_from_variant_id_summary200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


