# CodingVariants


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**ref** | **str** |  | 
**alt** | **str** |  | 
**protein_name** | **str** |  | 
**protein_id** | **str** |  | 
**gene_name** | **str** |  | 
**transcript_id** | **str** |  | 
**aapos** | **float** |  | 
**hgvsp** | **str** |  | 
**hgvsc** | **str** |  | [optional] 
**refcodon** | **str** |  | 
**codonpos** | **float** |  | 
**sift_score** | **float** |  | 
**sift4_g_score** | **float** |  | 
**polyphen2_hdiv_score** | **float** |  | 
**polyphen2_hvar_score** | **float** |  | 
**vest4_score** | **float** |  | 
**revel_score** | **float** |  | 
**mut_pred_score** | **float** |  | 
**bayes_del_add_af_score** | **float** |  | 
**bayes_del_no_af_score** | **float** |  | 
**varity_r_score** | **float** |  | 
**varity_er_score** | **float** |  | 
**varity_r_loo_score** | **float** |  | 
**varity_er_loo_score** | **float** |  | 
**esm1b_score** | **float** |  | 
**alpha_missense_score** | **float** |  | 
**cadd_raw_score** | **float** |  | 
**source** | **str** |  | 
**source_url** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.coding_variants import CodingVariants

# TODO update the JSON string below
json = "{}"
# create an instance of CodingVariants from a JSON string
coding_variants_instance = CodingVariants.from_json(json)
# print the JSON string representation of the object
print(CodingVariants.to_json())

# convert the object into a dict
coding_variants_dict = coding_variants_instance.to_dict()
# create an instance of CodingVariants from a dict
coding_variants_from_dict = CodingVariants.from_dict(coding_variants_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


