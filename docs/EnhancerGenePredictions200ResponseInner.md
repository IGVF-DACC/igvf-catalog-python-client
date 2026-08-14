# EnhancerGenePredictions200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gene** | [**GenomicElementsFromGenes200ResponseInnerGeneAnyOf**](GenomicElementsFromGenes200ResponseInnerGeneAnyOf.md) |  | 
**elements** | [**EnhancerGenePredictions200ResponseInnerElements**](EnhancerGenePredictions200ResponseInnerElements.md) |  | 

## Example

```python
from igvf_catalog_client.models.enhancer_gene_predictions200_response_inner import EnhancerGenePredictions200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of EnhancerGenePredictions200ResponseInner from a JSON string
enhancer_gene_predictions200_response_inner_instance = EnhancerGenePredictions200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(EnhancerGenePredictions200ResponseInner.to_json())

# convert the object into a dict
enhancer_gene_predictions200_response_inner_dict = enhancer_gene_predictions200_response_inner_instance.to_dict()
# create an instance of EnhancerGenePredictions200ResponseInner from a dict
enhancer_gene_predictions200_response_inner_from_dict = EnhancerGenePredictions200ResponseInner.from_dict(enhancer_gene_predictions200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


