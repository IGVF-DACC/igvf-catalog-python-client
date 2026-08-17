# DrugsFromVariants


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drug** | [**DrugsFromVariantsDrug**](DrugsFromVariantsDrug.md) |  | [optional] 
**var_from** | **str** |  | 
**gene_symbol** | **List[str]** |  | [optional] 
**pmid** | **str** |  | [optional] 
**study_parameters** | [**List[StudyParameters]**](StudyParameters.md) |  | [optional] 
**phenotype_categories** | **List[str]** |  | [optional] 
**source** | **str** |  | 
**source_url** | **str** |  | 
**name** | **str** |  | 
**var_class** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**files_filesets** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.drugs_from_variants import DrugsFromVariants

# TODO update the JSON string below
json = "{}"
# create an instance of DrugsFromVariants from a JSON string
drugs_from_variants_instance = DrugsFromVariants.from_json(json)
# print the JSON string representation of the object
print(DrugsFromVariants.to_json())

# convert the object into a dict
drugs_from_variants_dict = drugs_from_variants_instance.to_dict()
# create an instance of DrugsFromVariants from a dict
drugs_from_variants_from_dict = DrugsFromVariants.from_dict(drugs_from_variants_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


