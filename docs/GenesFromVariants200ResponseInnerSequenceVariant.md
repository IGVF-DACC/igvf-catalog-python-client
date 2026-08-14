# GenesFromVariants200ResponseInnerSequenceVariant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**chr** | **str** |  | 
**pos** | **float** |  | 
**rsid** | **List[str]** |  | [optional] 
**ref** | **str** |  | 
**alt** | **str** |  | 
**spdi** | **str** |  | [optional] 
**hgvs** | **str** |  | [optional] 
**ca_id** | **str** |  | [optional] 
**strain** | **List[str]** |  | [optional] 
**qual** | **str** |  | [optional] 
**files_filesets** | **str** |  | [optional] 
**annotations** | [**Variants200ResponseInnerAnnotations**](Variants200ResponseInnerAnnotations.md) |  | 
**source** | **str** |  | 
**source_url** | **str** |  | 
**organism** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.genes_from_variants200_response_inner_sequence_variant import GenesFromVariants200ResponseInnerSequenceVariant

# TODO update the JSON string below
json = "{}"
# create an instance of GenesFromVariants200ResponseInnerSequenceVariant from a JSON string
genes_from_variants200_response_inner_sequence_variant_instance = GenesFromVariants200ResponseInnerSequenceVariant.from_json(json)
# print the JSON string representation of the object
print(GenesFromVariants200ResponseInnerSequenceVariant.to_json())

# convert the object into a dict
genes_from_variants200_response_inner_sequence_variant_dict = genes_from_variants200_response_inner_sequence_variant_instance.to_dict()
# create an instance of GenesFromVariants200ResponseInnerSequenceVariant from a dict
genes_from_variants200_response_inner_sequence_variant_from_dict = GenesFromVariants200ResponseInnerSequenceVariant.from_dict(genes_from_variants200_response_inner_sequence_variant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


