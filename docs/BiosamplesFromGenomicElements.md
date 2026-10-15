# BiosamplesFromGenomicElements


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log2_fc** | **float** |  | 
**strand** | **str** |  | 
**neg_log10_pvalue** | **float** |  | 
**neg_log10_pvalue_adj** | **float** |  | 
**dna_count** | **float** |  | [optional] 
**rna_count** | **float** |  | [optional] 
**significant** | **bool** |  | [optional] 
**source** | **str** |  | [optional] 
**source_url** | **str** |  | [optional] 
**genomic_element** | [**BiosamplesFromGenomicElementsGenomicElement**](BiosamplesFromGenomicElementsGenomicElement.md) |  | [optional] 
**biosample** | [**BiosamplesFromGenomicElementsBiosample**](BiosamplesFromGenomicElementsBiosample.md) |  | [optional] 
**name** | **str** |  | 
**var_class** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**files_filesets** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.biosamples_from_genomic_elements import BiosamplesFromGenomicElements

# TODO update the JSON string below
json = "{}"
# create an instance of BiosamplesFromGenomicElements from a JSON string
biosamples_from_genomic_elements_instance = BiosamplesFromGenomicElements.from_json(json)
# print the JSON string representation of the object
print(BiosamplesFromGenomicElements.to_json())

# convert the object into a dict
biosamples_from_genomic_elements_dict = biosamples_from_genomic_elements_instance.to_dict()
# create an instance of BiosamplesFromGenomicElements from a dict
biosamples_from_genomic_elements_from_dict = BiosamplesFromGenomicElements.from_dict(biosamples_from_genomic_elements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


