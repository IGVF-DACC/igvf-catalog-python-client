# FilesFilesets


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
from igvf_catalog_client.models.files_filesets import FilesFilesets

# TODO update the JSON string below
json = "{}"
# create an instance of FilesFilesets from a JSON string
files_filesets_instance = FilesFilesets.from_json(json)
# print the JSON string representation of the object
print(FilesFilesets.to_json())

# convert the object into a dict
files_filesets_dict = files_filesets_instance.to_dict()
# create an instance of FilesFilesets from a dict
files_filesets_from_dict = FilesFilesets.from_dict(files_filesets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


