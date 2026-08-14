# PhenotypesFromCodingVariants200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coding_variant** | [**PhenotypesFromCodingVariants200ResponseInnerCodingVariant**](PhenotypesFromCodingVariants200ResponseInnerCodingVariant.md) |  | [optional] 
**phenotype** | [**PhenotypesFromCodingVariants200ResponseInnerPhenotype**](PhenotypesFromCodingVariants200ResponseInnerPhenotype.md) |  | [optional] 
**score** | **float** |  | 
**method** | **str** |  | [optional] 
**var_class** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**files_filesets** | **str** |  | [optional] 
**source** | **str** |  | 
**source_url** | **str** |  | 
**variant** | [**PhenotypesFromCodingVariants200ResponseInnerVariant**](PhenotypesFromCodingVariants200ResponseInnerVariant.md) |  | [optional] 

## Example

```python
from igvf_catalog_client.models.phenotypes_from_coding_variants200_response_inner import PhenotypesFromCodingVariants200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of PhenotypesFromCodingVariants200ResponseInner from a JSON string
phenotypes_from_coding_variants200_response_inner_instance = PhenotypesFromCodingVariants200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(PhenotypesFromCodingVariants200ResponseInner.to_json())

# convert the object into a dict
phenotypes_from_coding_variants200_response_inner_dict = phenotypes_from_coding_variants200_response_inner_instance.to_dict()
# create an instance of PhenotypesFromCodingVariants200ResponseInner from a dict
phenotypes_from_coding_variants200_response_inner_from_dict = PhenotypesFromCodingVariants200ResponseInner.from_dict(phenotypes_from_coding_variants200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


