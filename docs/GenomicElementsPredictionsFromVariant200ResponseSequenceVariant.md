# GenomicElementsPredictionsFromVariant200ResponseSequenceVariant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**chr** | **str** |  | 
**pos** | **float** |  | 
**rsid** | **List[str]** |  | 
**ref** | **str** |  | 
**alt** | **str** |  | 
**spdi** | **str** |  | 
**hgvs** | **str** |  | 
**ca_id** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.genomic_elements_predictions_from_variant200_response_sequence_variant import GenomicElementsPredictionsFromVariant200ResponseSequenceVariant

# TODO update the JSON string below
json = "{}"
# create an instance of GenomicElementsPredictionsFromVariant200ResponseSequenceVariant from a JSON string
genomic_elements_predictions_from_variant200_response_sequence_variant_instance = GenomicElementsPredictionsFromVariant200ResponseSequenceVariant.from_json(json)
# print the JSON string representation of the object
print(GenomicElementsPredictionsFromVariant200ResponseSequenceVariant.to_json())

# convert the object into a dict
genomic_elements_predictions_from_variant200_response_sequence_variant_dict = genomic_elements_predictions_from_variant200_response_sequence_variant_instance.to_dict()
# create an instance of GenomicElementsPredictionsFromVariant200ResponseSequenceVariant from a dict
genomic_elements_predictions_from_variant200_response_sequence_variant_from_dict = GenomicElementsPredictionsFromVariant200ResponseSequenceVariant.from_dict(genomic_elements_predictions_from_variant200_response_sequence_variant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


