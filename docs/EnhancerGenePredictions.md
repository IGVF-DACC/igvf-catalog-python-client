# EnhancerGenePredictions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gene** | [**GeneRef**](GeneRef.md) |  | 
**elements** | [**EnhancerGenePredictionsElements**](EnhancerGenePredictionsElements.md) |  | 

## Example

```python
from igvf_catalog_client.models.enhancer_gene_predictions import EnhancerGenePredictions

# TODO update the JSON string below
json = "{}"
# create an instance of EnhancerGenePredictions from a JSON string
enhancer_gene_predictions_instance = EnhancerGenePredictions.from_json(json)
# print the JSON string representation of the object
print(EnhancerGenePredictions.to_json())

# convert the object into a dict
enhancer_gene_predictions_dict = enhancer_gene_predictions_instance.to_dict()
# create an instance of EnhancerGenePredictions from a dict
enhancer_gene_predictions_from_dict = EnhancerGenePredictions.from_dict(enhancer_gene_predictions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


