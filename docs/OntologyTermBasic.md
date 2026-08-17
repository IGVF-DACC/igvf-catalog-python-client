# OntologyTermBasic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** |  | 
**term_id** | **str** |  | 
**name** | **str** |  | 
**synonyms** | **List[str]** |  | 
**description** | **str** |  | 
**source** | **str** |  | 
**subontology** | **str** |  | [optional] 
**var_class** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**files_filesets** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.ontology_term_basic import OntologyTermBasic

# TODO update the JSON string below
json = "{}"
# create an instance of OntologyTermBasic from a JSON string
ontology_term_basic_instance = OntologyTermBasic.from_json(json)
# print the JSON string representation of the object
print(OntologyTermBasic.to_json())

# convert the object into a dict
ontology_term_basic_dict = ontology_term_basic_instance.to_dict()
# create an instance of OntologyTermBasic from a dict
ontology_term_basic_from_dict = OntologyTermBasic.from_dict(ontology_term_basic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


