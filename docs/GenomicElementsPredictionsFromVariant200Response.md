# GenomicElementsPredictionsFromVariant200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sequence_variant** | [**GenomicElementsPredictionsFromVariant200ResponseSequenceVariant**](GenomicElementsPredictionsFromVariant200ResponseSequenceVariant.md) |  | 
**predictions** | [**GenomicElementsPredictionsFromVariant200ResponsePredictions**](GenomicElementsPredictionsFromVariant200ResponsePredictions.md) |  | 

## Example

```python
from igvf_catalog_client.models.genomic_elements_predictions_from_variant200_response import GenomicElementsPredictionsFromVariant200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GenomicElementsPredictionsFromVariant200Response from a JSON string
genomic_elements_predictions_from_variant200_response_instance = GenomicElementsPredictionsFromVariant200Response.from_json(json)
# print the JSON string representation of the object
print(GenomicElementsPredictionsFromVariant200Response.to_json())

# convert the object into a dict
genomic_elements_predictions_from_variant200_response_dict = genomic_elements_predictions_from_variant200_response_instance.to_dict()
# create an instance of GenomicElementsPredictionsFromVariant200Response from a dict
genomic_elements_predictions_from_variant200_response_from_dict = GenomicElementsPredictionsFromVariant200Response.from_dict(genomic_elements_predictions_from_variant200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


