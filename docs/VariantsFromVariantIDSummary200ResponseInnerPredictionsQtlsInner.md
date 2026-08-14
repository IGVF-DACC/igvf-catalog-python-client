# VariantsFromVariantIDSummary200ResponseInnerPredictionsQtlsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**cell_types** | [**List[VariantsFromVariantIDSummary200ResponseInnerPredictionsQtlsInnerCellTypesInner]**](VariantsFromVariantIDSummary200ResponseInnerPredictionsQtlsInnerCellTypesInner.md) |  | 
**genes** | [**List[VariantsFromVariantIDSummary200ResponseInnerPredictionsQtlsInnerGenesInner]**](VariantsFromVariantIDSummary200ResponseInnerPredictionsQtlsInnerGenesInner.md) |  | 

## Example

```python
from igvf_catalog_client.models.variants_from_variant_id_summary200_response_inner_predictions_qtls_inner import VariantsFromVariantIDSummary200ResponseInnerPredictionsQtlsInner

# TODO update the JSON string below
json = "{}"
# create an instance of VariantsFromVariantIDSummary200ResponseInnerPredictionsQtlsInner from a JSON string
variants_from_variant_id_summary200_response_inner_predictions_qtls_inner_instance = VariantsFromVariantIDSummary200ResponseInnerPredictionsQtlsInner.from_json(json)
# print the JSON string representation of the object
print(VariantsFromVariantIDSummary200ResponseInnerPredictionsQtlsInner.to_json())

# convert the object into a dict
variants_from_variant_id_summary200_response_inner_predictions_qtls_inner_dict = variants_from_variant_id_summary200_response_inner_predictions_qtls_inner_instance.to_dict()
# create an instance of VariantsFromVariantIDSummary200ResponseInnerPredictionsQtlsInner from a dict
variants_from_variant_id_summary200_response_inner_predictions_qtls_inner_from_dict = VariantsFromVariantIDSummary200ResponseInnerPredictionsQtlsInner.from_dict(variants_from_variant_id_summary200_response_inner_predictions_qtls_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


