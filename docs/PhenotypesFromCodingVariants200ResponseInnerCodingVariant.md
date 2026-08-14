# PhenotypesFromCodingVariants200ResponseInnerCodingVariant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**aapos** | **float** |  | [optional] 
**hgvsp** | **str** |  | [optional] 
**protein_name** | **str** |  | [optional] 
**gene_name** | **str** |  | [optional] 
**ref** | **str** |  | [optional] 
**alt** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.phenotypes_from_coding_variants200_response_inner_coding_variant import PhenotypesFromCodingVariants200ResponseInnerCodingVariant

# TODO update the JSON string below
json = "{}"
# create an instance of PhenotypesFromCodingVariants200ResponseInnerCodingVariant from a JSON string
phenotypes_from_coding_variants200_response_inner_coding_variant_instance = PhenotypesFromCodingVariants200ResponseInnerCodingVariant.from_json(json)
# print the JSON string representation of the object
print(PhenotypesFromCodingVariants200ResponseInnerCodingVariant.to_json())

# convert the object into a dict
phenotypes_from_coding_variants200_response_inner_coding_variant_dict = phenotypes_from_coding_variants200_response_inner_coding_variant_instance.to_dict()
# create an instance of PhenotypesFromCodingVariants200ResponseInnerCodingVariant from a dict
phenotypes_from_coding_variants200_response_inner_coding_variant_from_dict = PhenotypesFromCodingVariants200ResponseInnerCodingVariant.from_dict(phenotypes_from_coding_variants200_response_inner_coding_variant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


