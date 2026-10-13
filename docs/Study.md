# Study


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**ancestry_initial** | **str** |  | 
**ancestry_replication** | **str** |  | 
**n_cases** | **str** |  | 
**n_initial** | **str** |  | 
**n_replication** | **str** |  | 
**pmid** | **str** |  | 
**pub_author** | **str** |  | 
**pub_date** | **str** |  | 
**pub_journal** | **str** |  | 
**pub_title** | **str** |  | 
**has_sumstats** | **str** |  | 
**num_assoc_loci** | **str** |  | 
**study_source** | **str** |  | 
**trait_reported** | **str** |  | 
**trait_efos** | **str** |  | 
**trait_category** | **str** |  | 
**source** | **str** |  | [optional] 
**study_type** | **str** |  | 
**version** | **str** |  | 
**files_filesets** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.study import Study

# TODO update the JSON string below
json = "{}"
# create an instance of Study from a JSON string
study_instance = Study.from_json(json)
# print the JSON string representation of the object
print(Study.to_json())

# convert the object into a dict
study_dict = study_instance.to_dict()
# create an instance of Study from a dict
study_from_dict = Study.from_dict(study_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


