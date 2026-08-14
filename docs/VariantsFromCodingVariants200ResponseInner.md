# VariantsFromCodingVariants200ResponseInner


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
**id** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.variants_from_coding_variants200_response_inner import VariantsFromCodingVariants200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of VariantsFromCodingVariants200ResponseInner from a JSON string
variants_from_coding_variants200_response_inner_instance = VariantsFromCodingVariants200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(VariantsFromCodingVariants200ResponseInner.to_json())

# convert the object into a dict
variants_from_coding_variants200_response_inner_dict = variants_from_coding_variants200_response_inner_instance.to_dict()
# create an instance of VariantsFromCodingVariants200ResponseInner from a dict
variants_from_coding_variants200_response_inner_from_dict = VariantsFromCodingVariants200ResponseInner.from_dict(variants_from_coding_variants200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


