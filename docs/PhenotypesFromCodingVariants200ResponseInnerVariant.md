# PhenotypesFromCodingVariants200ResponseInnerVariant


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
from igvf_catalog_client.models.phenotypes_from_coding_variants200_response_inner_variant import PhenotypesFromCodingVariants200ResponseInnerVariant

# TODO update the JSON string below
json = "{}"
# create an instance of PhenotypesFromCodingVariants200ResponseInnerVariant from a JSON string
phenotypes_from_coding_variants200_response_inner_variant_instance = PhenotypesFromCodingVariants200ResponseInnerVariant.from_json(json)
# print the JSON string representation of the object
print(PhenotypesFromCodingVariants200ResponseInnerVariant.to_json())

# convert the object into a dict
phenotypes_from_coding_variants200_response_inner_variant_dict = phenotypes_from_coding_variants200_response_inner_variant_instance.to_dict()
# create an instance of PhenotypesFromCodingVariants200ResponseInnerVariant from a dict
phenotypes_from_coding_variants200_response_inner_variant_from_dict = PhenotypesFromCodingVariants200ResponseInnerVariant.from_dict(phenotypes_from_coding_variants200_response_inner_variant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


