# GenesProteinsFromVariants200ResponseInnerSequenceVariant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**chr** | **str** |  | 
**pos** | **float** |  | 
**rsid** | **List[str]** |  | [optional] 
**ref** | **str** |  | 
**alt** | **str** |  | 
**spdi** | **str** |  | 
**hgvs** | **str** |  | 
**ca_id** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.genes_proteins_from_variants200_response_inner_sequence_variant import GenesProteinsFromVariants200ResponseInnerSequenceVariant

# TODO update the JSON string below
json = "{}"
# create an instance of GenesProteinsFromVariants200ResponseInnerSequenceVariant from a JSON string
genes_proteins_from_variants200_response_inner_sequence_variant_instance = GenesProteinsFromVariants200ResponseInnerSequenceVariant.from_json(json)
# print the JSON string representation of the object
print(GenesProteinsFromVariants200ResponseInnerSequenceVariant.to_json())

# convert the object into a dict
genes_proteins_from_variants200_response_inner_sequence_variant_dict = genes_proteins_from_variants200_response_inner_sequence_variant_instance.to_dict()
# create an instance of GenesProteinsFromVariants200ResponseInnerSequenceVariant from a dict
genes_proteins_from_variants200_response_inner_sequence_variant_from_dict = GenesProteinsFromVariants200ResponseInnerSequenceVariant.from_dict(genes_proteins_from_variants200_response_inner_sequence_variant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


