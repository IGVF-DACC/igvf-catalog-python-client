# GenomicElementsPredictionsFromVariant200ResponsePredictions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cell_types** | **List[str]** |  | 
**genes** | [**List[GenomicElementsPredictionsFromVariant200ResponsePredictionsGenesInner]**](GenomicElementsPredictionsFromVariant200ResponsePredictionsGenesInner.md) |  | 

## Example

```python
from igvf_catalog_client.models.genomic_elements_predictions_from_variant200_response_predictions import GenomicElementsPredictionsFromVariant200ResponsePredictions

# TODO update the JSON string below
json = "{}"
# create an instance of GenomicElementsPredictionsFromVariant200ResponsePredictions from a JSON string
genomic_elements_predictions_from_variant200_response_predictions_instance = GenomicElementsPredictionsFromVariant200ResponsePredictions.from_json(json)
# print the JSON string representation of the object
print(GenomicElementsPredictionsFromVariant200ResponsePredictions.to_json())

# convert the object into a dict
genomic_elements_predictions_from_variant200_response_predictions_dict = genomic_elements_predictions_from_variant200_response_predictions_instance.to_dict()
# create an instance of GenomicElementsPredictionsFromVariant200ResponsePredictions from a dict
genomic_elements_predictions_from_variant200_response_predictions_from_dict = GenomicElementsPredictionsFromVariant200ResponsePredictions.from_dict(genomic_elements_predictions_from_variant200_response_predictions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


