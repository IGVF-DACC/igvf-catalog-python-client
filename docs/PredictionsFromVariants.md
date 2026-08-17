# PredictionsFromVariants


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
**target_gene** | [**TargetGene**](TargetGene.md) |  | 
**score** | **float** |  | [optional] 
**model** | **str** |  | 
**dataset** | **str** |  | 
**name** | **str** |  | 
**files_filesets** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.predictions_from_variants import PredictionsFromVariants

# TODO update the JSON string below
json = "{}"
# create an instance of PredictionsFromVariants from a JSON string
predictions_from_variants_instance = PredictionsFromVariants.from_json(json)
# print the JSON string representation of the object
print(PredictionsFromVariants.to_json())

# convert the object into a dict
predictions_from_variants_dict = predictions_from_variants_instance.to_dict()
# create an instance of PredictionsFromVariants from a dict
predictions_from_variants_from_dict = PredictionsFromVariants.from_dict(predictions_from_variants_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


