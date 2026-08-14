# ProteinsFromVariants200ResponseInnerSequenceVariant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chr** | **str** |  | 
**pos** | **float** |  | 
**ref** | **str** |  | 
**alt** | **str** |  | 
**rsid** | **List[str]** |  | [optional] 
**spdi** | **str** |  | [optional] 
**hgvs** | **str** |  | [optional] 
**ca_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.proteins_from_variants200_response_inner_sequence_variant import ProteinsFromVariants200ResponseInnerSequenceVariant

# TODO update the JSON string below
json = "{}"
# create an instance of ProteinsFromVariants200ResponseInnerSequenceVariant from a JSON string
proteins_from_variants200_response_inner_sequence_variant_instance = ProteinsFromVariants200ResponseInnerSequenceVariant.from_json(json)
# print the JSON string representation of the object
print(ProteinsFromVariants200ResponseInnerSequenceVariant.to_json())

# convert the object into a dict
proteins_from_variants200_response_inner_sequence_variant_dict = proteins_from_variants200_response_inner_sequence_variant_instance.to_dict()
# create an instance of ProteinsFromVariants200ResponseInnerSequenceVariant from a dict
proteins_from_variants200_response_inner_sequence_variant_from_dict = ProteinsFromVariants200ResponseInnerSequenceVariant.from_dict(proteins_from_variants200_response_inner_sequence_variant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


