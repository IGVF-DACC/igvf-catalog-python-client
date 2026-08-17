# BiosamplesFromGenomicElementsBiosample


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** |  | 
**term_id** | **str** |  | 
**name** | **str** |  | 
**synonyms** | **List[str]** |  | [optional] 
**description** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**subontology** | **str** |  | [optional] 
**source_url** | **str** |  | [optional] 
**var_class** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**files_filesets** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.biosamples_from_genomic_elements_biosample import BiosamplesFromGenomicElementsBiosample

# TODO update the JSON string below
json = "{}"
# create an instance of BiosamplesFromGenomicElementsBiosample from a JSON string
biosamples_from_genomic_elements_biosample_instance = BiosamplesFromGenomicElementsBiosample.from_json(json)
# print the JSON string representation of the object
print(BiosamplesFromGenomicElementsBiosample.to_json())

# convert the object into a dict
biosamples_from_genomic_elements_biosample_dict = biosamples_from_genomic_elements_biosample_instance.to_dict()
# create an instance of BiosamplesFromGenomicElementsBiosample from a dict
biosamples_from_genomic_elements_biosample_from_dict = BiosamplesFromGenomicElementsBiosample.from_dict(biosamples_from_genomic_elements_biosample_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


