# GenesProteinsFromVariants200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sequence_variant** | [**GenesProteinsFromVariants200ResponseInnerSequenceVariant**](GenesProteinsFromVariants200ResponseInnerSequenceVariant.md) |  | 
**related** | [**List[GenesProteinsFromVariants200ResponseInnerRelatedInner]**](GenesProteinsFromVariants200ResponseInnerRelatedInner.md) |  | 

## Example

```python
from igvf_catalog_client.models.genes_proteins_from_variants200_response_inner import GenesProteinsFromVariants200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GenesProteinsFromVariants200ResponseInner from a JSON string
genes_proteins_from_variants200_response_inner_instance = GenesProteinsFromVariants200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GenesProteinsFromVariants200ResponseInner.to_json())

# convert the object into a dict
genes_proteins_from_variants200_response_inner_dict = genes_proteins_from_variants200_response_inner_instance.to_dict()
# create an instance of GenesProteinsFromVariants200ResponseInner from a dict
genes_proteins_from_variants200_response_inner_from_dict = GenesProteinsFromVariants200ResponseInner.from_dict(genes_proteins_from_variants200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


