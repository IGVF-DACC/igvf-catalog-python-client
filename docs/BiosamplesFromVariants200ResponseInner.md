# BiosamplesFromVariants200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variant** | [**BiosamplesFromVariants200ResponseInnerVariant**](BiosamplesFromVariants200ResponseInnerVariant.md) |  | [optional] 
**biosample** | [**DiseaseFromVariants200ResponseInnerDisease**](DiseaseFromVariants200ResponseInnerDisease.md) |  | [optional] 
**genomic_element** | [**BiosamplesFromVariants200ResponseInnerGenomicElement**](BiosamplesFromVariants200ResponseInnerGenomicElement.md) |  | [optional] 
**strand** | **str** |  | [optional] 
**log2_fc** | **float** |  | [optional] 
**dna_count_ref** | **float** |  | [optional] 
**dna_count_alt** | **float** |  | [optional] 
**rna_count_ref** | **float** |  | [optional] 
**rna_count_alt** | **float** |  | [optional] 
**post_prob_effect** | **float** |  | [optional] 
**ci_lower_95** | **float** |  | [optional] 
**ci_upper_95** | **float** |  | [optional] 
**significant** | **bool** |  | [optional] 
**neg_log10_pvalue** | **float** |  | [optional] 
**neg_log10_pvalue_adj** | **float** |  | [optional] 
**label** | **str** |  | 
**method** | **str** |  | 
**var_class** | **str** |  | [optional] 
**source** | **str** |  | 
**source_url** | **str** |  | 
**name** | **str** |  | 
**files_filesets** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.biosamples_from_variants200_response_inner import BiosamplesFromVariants200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of BiosamplesFromVariants200ResponseInner from a JSON string
biosamples_from_variants200_response_inner_instance = BiosamplesFromVariants200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(BiosamplesFromVariants200ResponseInner.to_json())

# convert the object into a dict
biosamples_from_variants200_response_inner_dict = biosamples_from_variants200_response_inner_instance.to_dict()
# create an instance of BiosamplesFromVariants200ResponseInner from a dict
biosamples_from_variants200_response_inner_from_dict = BiosamplesFromVariants200ResponseInner.from_dict(biosamples_from_variants200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


