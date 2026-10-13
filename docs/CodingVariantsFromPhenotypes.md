# CodingVariantsFromPhenotypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coding_variant** | [**CodingVariant**](CodingVariant.md) |  | [optional] 
**phenotype** | [**PhenotypeRef**](PhenotypeRef.md) |  | [optional] 
**score** | **float** |  | 
**method** | **str** |  | [optional] 
**var_class** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**files_filesets** | **str** |  | [optional] 
**source** | **str** |  | 
**source_url** | **str** |  | 
**variant** | [**VariantBasic**](VariantBasic.md) |  | [optional] 

## Example

```python
from igvf_catalog_client.models.coding_variants_from_phenotypes import CodingVariantsFromPhenotypes

# TODO update the JSON string below
json = "{}"
# create an instance of CodingVariantsFromPhenotypes from a JSON string
coding_variants_from_phenotypes_instance = CodingVariantsFromPhenotypes.from_json(json)
# print the JSON string representation of the object
print(CodingVariantsFromPhenotypes.to_json())

# convert the object into a dict
coding_variants_from_phenotypes_dict = coding_variants_from_phenotypes_instance.to_dict()
# create an instance of CodingVariantsFromPhenotypes from a dict
coding_variants_from_phenotypes_from_dict = CodingVariantsFromPhenotypes.from_dict(coding_variants_from_phenotypes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


