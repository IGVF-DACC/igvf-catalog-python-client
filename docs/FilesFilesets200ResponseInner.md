# FilesFilesets200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**file_set_id** | **str** |  | 
**lab** | **str** |  | 
**preferred_assay_titles** | **List[str]** |  | [optional] 
**assay_term_ids** | **List[str]** |  | [optional] 
**method** | **str** |  | [optional] 
**var_class** | **str** |  | 
**software** | **List[str]** |  | [optional] 
**collections** | **List[str]** |  | [optional] 
**samples** | **List[str]** |  | [optional] 
**sample_ids** | **List[str]** |  | [optional] 
**simple_sample_summaries** | **List[str]** |  | [optional] 
**donors** | **List[str]** |  | [optional] 
**source** | **str** |  | 
**source_url** | **str** |  | [optional] 
**download_link** | **str** |  | 
**cell_annotation** | **str** |  | [optional] 
**cell_annotation_term** | **str** |  | [optional] 
**genome_browser_link** | **str** |  | [optional] 
**crispr_modality** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.files_filesets200_response_inner import FilesFilesets200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of FilesFilesets200ResponseInner from a JSON string
files_filesets200_response_inner_instance = FilesFilesets200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(FilesFilesets200ResponseInner.to_json())

# convert the object into a dict
files_filesets200_response_inner_dict = files_filesets200_response_inner_instance.to_dict()
# create an instance of FilesFilesets200ResponseInner from a dict
files_filesets200_response_inner_from_dict = FilesFilesets200ResponseInner.from_dict(files_filesets200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


