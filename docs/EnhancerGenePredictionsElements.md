# EnhancerGenePredictionsElements


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**cell_type** | **str** |  | [optional] 
**score** | **float** |  | [optional] 
**model** | **str** |  | [optional] 
**dataset** | **str** |  | [optional] 
**element_type** | **str** |  | [optional] 
**element_chr** | **str** |  | [optional] 
**element_start** | **float** |  | [optional] 
**element_end** | **float** |  | [optional] 
**name** | **str** |  | 
**method** | **str** |  | [optional] 
**var_class** | **str** |  | [optional] 
**files_filesets** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.enhancer_gene_predictions_elements import EnhancerGenePredictionsElements

# TODO update the JSON string below
json = "{}"
# create an instance of EnhancerGenePredictionsElements from a JSON string
enhancer_gene_predictions_elements_instance = EnhancerGenePredictionsElements.from_json(json)
# print the JSON string representation of the object
print(EnhancerGenePredictionsElements.to_json())

# convert the object into a dict
enhancer_gene_predictions_elements_dict = enhancer_gene_predictions_elements_instance.to_dict()
# create an instance of EnhancerGenePredictionsElements from a dict
enhancer_gene_predictions_elements_from_dict = EnhancerGenePredictionsElements.from_dict(enhancer_gene_predictions_elements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


