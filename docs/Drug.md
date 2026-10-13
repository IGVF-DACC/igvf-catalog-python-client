# Drug


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
from igvf_catalog_client.models.drug import Drug

# TODO update the JSON string below
json = "{}"
# create an instance of Drug from a JSON string
drug_instance = Drug.from_json(json)
# print the JSON string representation of the object
print(Drug.to_json())

# convert the object into a dict
drug_dict = drug_instance.to_dict()
# create an instance of Drug from a dict
drug_from_dict = Drug.from_dict(drug_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


