# BiosamplesFromVariants200ResponseInnerVariant


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
from igvf_catalog_client.models.biosamples_from_variants200_response_inner_variant import BiosamplesFromVariants200ResponseInnerVariant

# TODO update the JSON string below
json = "{}"
# create an instance of BiosamplesFromVariants200ResponseInnerVariant from a JSON string
biosamples_from_variants200_response_inner_variant_instance = BiosamplesFromVariants200ResponseInnerVariant.from_json(json)
# print the JSON string representation of the object
print(BiosamplesFromVariants200ResponseInnerVariant.to_json())

# convert the object into a dict
biosamples_from_variants200_response_inner_variant_dict = biosamples_from_variants200_response_inner_variant_instance.to_dict()
# create an instance of BiosamplesFromVariants200ResponseInnerVariant from a dict
biosamples_from_variants200_response_inner_variant_from_dict = BiosamplesFromVariants200ResponseInnerVariant.from_dict(biosamples_from_variants200_response_inner_variant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


