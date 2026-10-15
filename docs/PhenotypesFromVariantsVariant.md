# PhenotypesFromVariantsVariant


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
from igvf_catalog_client.models.phenotypes_from_variants_variant import PhenotypesFromVariantsVariant

# TODO update the JSON string below
json = "{}"
# create an instance of PhenotypesFromVariantsVariant from a JSON string
phenotypes_from_variants_variant_instance = PhenotypesFromVariantsVariant.from_json(json)
# print the JSON string representation of the object
print(PhenotypesFromVariantsVariant.to_json())

# convert the object into a dict
phenotypes_from_variants_variant_dict = phenotypes_from_variants_variant_instance.to_dict()
# create an instance of PhenotypesFromVariantsVariant from a dict
phenotypes_from_variants_variant_from_dict = PhenotypesFromVariantsVariant.from_dict(phenotypes_from_variants_variant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


