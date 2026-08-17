# DrugsFromVariantsDrug


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**drug_ontology_terms** | **List[str]** |  | [optional] 
**source** | **str** |  | 
**source_url** | **str** |  | 
**var_class** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**files_filesets** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.drugs_from_variants_drug import DrugsFromVariantsDrug

# TODO update the JSON string below
json = "{}"
# create an instance of DrugsFromVariantsDrug from a JSON string
drugs_from_variants_drug_instance = DrugsFromVariantsDrug.from_json(json)
# print the JSON string representation of the object
print(DrugsFromVariantsDrug.to_json())

# convert the object into a dict
drugs_from_variants_drug_dict = drugs_from_variants_drug_instance.to_dict()
# create an instance of DrugsFromVariantsDrug from a dict
drugs_from_variants_drug_from_dict = DrugsFromVariantsDrug.from_dict(drugs_from_variants_drug_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


