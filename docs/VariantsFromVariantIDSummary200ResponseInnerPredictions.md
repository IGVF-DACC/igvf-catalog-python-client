# VariantsFromVariantIDSummary200ResponseInnerPredictions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**qtls** | [**List[VariantsFromVariantIDSummary200ResponseInnerPredictionsQtlsInner]**](VariantsFromVariantIDSummary200ResponseInnerPredictionsQtlsInner.md) |  | [optional] 
**tf_binding** | [**List[VariantsFromVariantIDSummary200ResponseInnerPredictionsTfBindingInner]**](VariantsFromVariantIDSummary200ResponseInnerPredictionsTfBindingInner.md) |  | [optional] 

## Example

```python
from igvf_catalog_client.models.variants_from_variant_id_summary200_response_inner_predictions import VariantsFromVariantIDSummary200ResponseInnerPredictions

# TODO update the JSON string below
json = "{}"
# create an instance of VariantsFromVariantIDSummary200ResponseInnerPredictions from a JSON string
variants_from_variant_id_summary200_response_inner_predictions_instance = VariantsFromVariantIDSummary200ResponseInnerPredictions.from_json(json)
# print the JSON string representation of the object
print(VariantsFromVariantIDSummary200ResponseInnerPredictions.to_json())

# convert the object into a dict
variants_from_variant_id_summary200_response_inner_predictions_dict = variants_from_variant_id_summary200_response_inner_predictions_instance.to_dict()
# create an instance of VariantsFromVariantIDSummary200ResponseInnerPredictions from a dict
variants_from_variant_id_summary200_response_inner_predictions_from_dict = VariantsFromVariantIDSummary200ResponseInnerPredictions.from_dict(variants_from_variant_id_summary200_response_inner_predictions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


