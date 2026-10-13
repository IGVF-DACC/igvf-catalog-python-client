# GenomicElementsPredictionsFromVariant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sequence_variant** | [**VariantBasic**](VariantBasic.md) |  | 
**predictions** | [**Predictions**](Predictions.md) |  | 

## Example

```python
from igvf_catalog_client.models.genomic_elements_predictions_from_variant import GenomicElementsPredictionsFromVariant

# TODO update the JSON string below
json = "{}"
# create an instance of GenomicElementsPredictionsFromVariant from a JSON string
genomic_elements_predictions_from_variant_instance = GenomicElementsPredictionsFromVariant.from_json(json)
# print the JSON string representation of the object
print(GenomicElementsPredictionsFromVariant.to_json())

# convert the object into a dict
genomic_elements_predictions_from_variant_dict = genomic_elements_predictions_from_variant_instance.to_dict()
# create an instance of GenomicElementsPredictionsFromVariant from a dict
genomic_elements_predictions_from_variant_from_dict = GenomicElementsPredictionsFromVariant.from_dict(genomic_elements_predictions_from_variant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


