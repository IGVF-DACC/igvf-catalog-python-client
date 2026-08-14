# PredictionsFromVariants200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distance_gene_variant** | **float** |  | 
**element_chr** | **str** |  | 
**element_start** | **float** |  | 
**element_end** | **float** |  | 
**element_type** | **str** |  | 
**id** | **str** |  | 
**cell_type** | **str** |  | 
**target_gene** | [**PredictionsFromVariants200ResponseInnerTargetGene**](PredictionsFromVariants200ResponseInnerTargetGene.md) |  | 
**score** | **float** |  | [optional] 
**model** | **str** |  | 
**dataset** | **str** |  | 
**name** | **str** |  | 
**files_filesets** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.predictions_from_variants200_response_inner import PredictionsFromVariants200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of PredictionsFromVariants200ResponseInner from a JSON string
predictions_from_variants200_response_inner_instance = PredictionsFromVariants200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(PredictionsFromVariants200ResponseInner.to_json())

# convert the object into a dict
predictions_from_variants200_response_inner_dict = predictions_from_variants200_response_inner_instance.to_dict()
# create an instance of PredictionsFromVariants200ResponseInner from a dict
predictions_from_variants200_response_inner_from_dict = PredictionsFromVariants200ResponseInner.from_dict(predictions_from_variants200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


