# gridpacks
Repository for generating gridpacks with reweighting with amcatnlo 

Card templates can be found in the path addons/cards/UFOMODEL_template and the corresponding UFO file in addons/models
to generate a gridpack run "source submit_madpack_ttbareft.sh"
this will copy the template and replace settings in the default templates if needded according to what is specified 
in the submit script 
modify customize card to change the corresponding operators you want to use
the example gridpack gluontop_rwgt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz was tested in debug which 
also contains an example lhe output with EFT and systematics weights   

## Generate multiple gridpacks
To generate more than one gridpack use submit_gridpacks.sh

Before you start create a cms environment using the following commands:
```
cmsrel CMSSW_9_4_6_patch1
cd CMSSW_9_4_6_patch1/src
cmsenv
export CMSSW_BASE=
```
Define the following parameters in submit_gridpacks.sh:
```
states to analyze (e.g. ttZ ttgamma) <-- make sure you have all cards in addons/cards/
declare number of jets (--> cardname e.g. ttZ0j_rwgt)
declare polynomial order (e.g. 2nd, 3rd, 4th)
lxplus GRID (where to calculate)
dim6 operators and stepsize as string (e.g. 'ctZ 1 ctZI 1')
referencepoint as string (e.g. 'ctZ 4 ctZI 4')
```
  
  
## List of available gridpacks:  
  
The script will loop over all states to analyze and create a directory structure in the output directory containing the calculated gridpacks, customizecards (with defined reference point) and pkl file
Available gridpacks, pkl files, customize cards and STDOUTs stored at:  
```  
/afs/hephy.at/data/llechner01/TTXPheno/gridpacks/<date>/<process>/order<poly order>/  
```  
   
  
### 13/08/2018  
large full ttbar sample

| process  | poly order | # coeff | Wilson coefficients     | Link to gen. events  |
|:--------:|:----------:|:-------:|:-----------------------:|:--------------------:|
| tt_full  | -           | 0       | no WC                  | [10M WZ events](https://cmsweb.cern.ch/das/request?input=%2Ftt_full_rwgt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball%2Fllechner-tt_dim6top_13Aug18-c2f0c52481627e66edabf074e5458056%2FUSER&instance=prod%2Fphys03) | 
   
  
### 31/07/2018  TC
##### Run Card changed! (directory 31072018_TC)  
ttgamma gridpacks for semi-/di-leptonic cases    
Run Card according to Tom Cornelis (TC)! Talk given in Top Properties on March 7th 2018  
Run Card stored in the gridpack directory  
Reference Point: ctW = 4., ctWI = 4., ctZ = 4., ctZI = 4., ctG = 4., ctGI = 4.  

| process  | poly order | # coeff | Wilson coefficients  | Link to gen. events  |  
|:--------:|:----------:|:-------:|:--------------------:|:--------------------:|  
| ttgamma 1l | 2          | 8       | cpQM, cpt, ctW, ctWI, ctZ, ctZI, ctG, ctGI | [1M ttgamma1l events](https://cmsweb.cern.ch/das/request?input=%2Fttgamma1l_rwgt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball%2Fllechner-ttTC_dim6top_31July18-7211d47a05942de63b96d242b817a8bb%2FUSER&instance=prod%2Fphys03) |
| ttgamma 2l | 2          | 8       | cpQM, cpt, ctW, ctWI, ctZ, ctZI, ctG, ctGI | [1M ttgamma2l events](https://cmsweb.cern.ch/das/request?input=%2Fttgamma2l_rwgt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball%2Fllechner-ttTC_dim6top_31July18-0a43f57f51d88147b253bdf1fa82c508%2FUSER&instance=prod%2Fphys03) |
  
  
### 31/07/2018  
ttgamma gridpacks for semi-/di-leptonic cases    
Reference Point: ctW = 4., ctWI = 4., ctZ = 4., ctZI = 4., ctG = 4., ctGI = 4.  

| process  | poly order | # coeff | Wilson coefficients  | Link to gen. events  |  
|:--------:|:----------:|:-------:|:--------------------:|:--------------------:|  
| ttgamma 1l | 2          | 8       | cpQM, cpt, ctW, ctWI, ctZ, ctZI, ctG, ctGI | not (yet) processed!  |
| ttgamma 2l | 2          | 8       | cpQM, cpt, ctW, ctWI, ctZ, ctZI, ctG, ctGI | not (yet) processed!  |
  
  
### 06/07/2018  
Background gridpacks (leptonic)  

| process  | poly order | # coeff | Wilson coefficients                                                                 | Link to gen. events  |
|:--------:|:----------:|:-------:|:-----------------------------------------------------------------------------------:|:--------------------:|
| WZ (lep)     | -           | 0       | no WC | [1M WZ events](https://cmsweb.cern.ch/das/request?input=%2FWZ_lep_rwgt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball%2Fllechner-bg_dim6top_06July18-6dade6042d6868e7bb87de85663e8a54%2FUSER&instance=prod%2Fphys03) | 
| ttbar (lep)  | -           | 0       | no WC | [1M ttbar events](https://cmsweb.cern.ch/das/request?input=%2Ftt_lep_rwgt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball%2Fllechner-bg_lep_dim6top_06July18-399ed716eb7225402bb4416ff36fe4d6%2FUSER&instance=prod%2Fphys03) | 
| ttbar (semilep)  | -           | 0       | no WC | [1M ttbar events](https://cmsweb.cern.ch/das/request?input=%2Ftt_semilep_rwgt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball%2Fllechner-bg_dim6top_06July18-61f6d1f3cc6e0e3d29066ed21db166d3%2FUSER&instance=prod%2Fphys03) | 
| tWZ          | -           | 0       | no WC | [1M tWZ events](https://cmsweb.cern.ch/das/request?input=%2FtWZ_rwgt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball%2Fllechner-bg_dim6top_06July18-083eb65e1bdfcfc8fcf3d4f572bc27da%2FUSER&instance=prod%2Fphys03) | 
| ttgamma      | -           | 0       | no WC | [1M ttgamma events](https://cmsweb.cern.ch/das/request?input=%2Fttgamma_rwgt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball%2Fllechner-bg_lep_dim6top_06July18-7c92494a0b9e35a525af35a2e83e005b%2FUSER&instance=prod%2Fphys03) | 
| tZq          | -           | 0       | no WC | [1M tZq events](https://cmsweb.cern.ch/das/request?input=%2FtZq_rwgt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball%2Fllechner-bg_lep_dim6top_06July18-622c407898c13833e0c43092e83c38c5%2FUSER&instance=prod%2Fphys03) | 
| Zgamma       | -           | 0       | no WC | [1M Zgamma events](https://cmsweb.cern.ch/das/request?input=%2FZgamma_rwgt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball%2Fllechner-bg_dim6top_06July18-d4a3491b99ce351d59c2f3c59adf0bd3%2FUSER&instance=prod%2Fphys03) | 
| tW           | -           | 0       | no WC | [1M tW events](https://cmsweb.cern.ch/das/request?input=%2FtW_rwgt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball%2Fllechner-bg_dim6top_06July18-c93c9d5de5b5d5ea926359481176f094%2FUSER&instance=prod%2Fphys03) | 
  
  
### 27/06/2018  
##### Reference Point (directory 27062018_ref)  
4 Fermion WC gridpacks for 3rd gen quarks with 1st/2nd gen leps  
Reference Point: ctW = 4., ctWI = 4., ctZ = 4., ctZI = 4., cQl31 = 4., cQlM1 = 4., ctlS1 = 4., ctlSI1 = 4., ctlT1 = 4., ctlTI1 = 4., cQl32 = 4., cQlM2 = 4., ctlS2 = 4., ctlSI2 = 4., ctlT2 = 4., ctlTI2 = 4.  
  
| process  | poly order | # coeff | Wilson coefficients  | Link to gen. events |
|:--------:|:----------:|:-------:|:--------------------:|:-------------------:|
| ttZ      | 2          | 18      | cpQM, cpt, ctW, ctWI, ctZ, ctZI, cQl31, cQlM1, ctlS1, ctlSI1, ctlT1, ctlTI1, cQl32, cQlM2, ctlS2, ctlSI2, ctlT2, ctlTI2 | not (yet) processed  |
  
  
### 26/06/2018  
##### Reference Point (directory 26062018_ref)  
4th order WC gridpacks  
Reference Point: ctW = 4., ctWI = 4., ctZ = 4., ctZI = 4.  
  
| process  | poly order | # coeff | Wilson coefficients  | Link to gen. events |  
|:--------:|:----------:|:-------:|:--------------------:|:-------------------:|  
| ttZ      | 4          | 6       | cpQM, cpt, ctW, ctWI, ctZ, ctZI | not (yet) processed!  |  
| ttW      | 4          | 6       | cpQM, cpt, ctW, ctWI, ctZ, ctZI | not (yet) processed!  |  
| ttgamma  | 4          | 6       | cpQM, cpt, ctW, ctWI, ctZ, ctZI | not (yet) processed!  |  
  
  
### 14/06/2018  
##### Reference Point (directory 14062018_ref)  
4 Fermion WC gridpacks (test)  
Reference Point: ctZ = 4., ctZI = 4., cQl31 = 4., cQlM1 = 4., cQl32 = 4., cQlM2 = 4.  
  
| process  | poly order | # coeff | Wilson coefficients                                                                 | Link to gen. events |
|:--------:|:----------:|:-------:|:------------------------------------------------:|:--------------------:|
| ttZ      | 2          | 8       | cpQM, cpt, ctZ, ctZI, cQl31, cQlM1, cQl32, cQlM2 | not (yet) processed  |
  
  
### 05/06/2018  
##### Reference Point (directory 05062018_ref)  
Background gridpacks (leptonic)  
t > b W > b l nu  

| process  | poly order | # coeff | Wilson coefficients                                                                 | Link to gen. events  |
|:--------:|:----------:|:-------:|:-----------------------------------------------------------------------------------:|:--------------------:|
| ttbar (lep)  | 2           | 15      | ctp, ctpI, cpQM, cpQ3, cpt, cptb, cptbI, ctW, ctWI, ctZ, ctZI, cbW, cbWI, ctG, ctGI | [1M ttbar events](https://cmsweb.cern.ch/das/request?input=%2Ftt_lep_rwgt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball%2Fllechner-bg_lep_dim6top_05June18-399ed716eb7225402bb4416ff36fe4d6%2FUSER&instance=prod%2Fphys03) | 
  
  
### 04/06/2018  
Background gridpacks (hadronic + leptonic)

| process  | poly order | # coeff | Wilson coefficients                                                                 | Link to gen. events  |
|:--------:|:----------:|:-------:|:-----------------------------------------------------------------------------------:|:--------------------:|
| WZ (all)     | 2           | 0       | no relevant WC                                                                      | [1M WZ events](https://cmsweb.cern.ch/das/request?input=%2FWZ_rwgt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball%2Fllechner-bg_dim6top_04June18-a4eb1cf113188459e4c517c4aa52c31c%2FUSER&instance=prod%2Fphys03) | 
| ttbar (all)  | 2           | 15      | ctp, ctpI, cpQM, cpQ3, cpt, cptb, cptbI, ctW, ctWI, ctZ, ctZI, cbW, cbWI, ctG, ctGI | [1M ttbar events](https://cmsweb.cern.ch/das/request?input=%2Ftt_rwgt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball%2Fllechner-bg_dim6top_04June18-db4155f01c4c21dc10125760597b536e%2FUSER&instance=prod%2Fphys03) | 
  
  
### 18/05/2018  

| process  | poly order | # coeff | Wilson coefficients                                                                 | Link to gen. events |
|:--------:|:----------:|:-------:|:-----------------------------------------------------------------------------------:|:------------------------:|
| ttZ      | 2          | 15      | ctp, ctpI, cpQM, cpQ3, cpt, cptb, cptbI, ctW, ctWI, ctZ, ctZI, cbW, cbWI, ctG, ctGI | [1M ttZ events](https://cmsweb.cern.ch/das/request?input=%2FttZ0j_rwgt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball%2Fllechner-ttZ0j_order2_15weights_18052018-7a5fde3f5bf89006ee3acec926ca87d8%2FUSER&instance=prod%2Fphys03)  |
| ttW      | 2          | 15      | ctp, ctpI, cpQM, cpQ3, cpt, cptb, cptbI, ctW, ctWI, ctZ, ctZI, cbW, cbWI, ctG, ctGI | [1M ttW events](https://cmsweb.cern.ch/das/request?input=%2FttW0j_rwgt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball%2Fllechner-ttW0j_order2_15weights_18052018-593ea75549b4c51667dffc93040bbda1%2FUSER&instance=prod%2Fphys03)  |
| ttgamma  | 2          | 15      | ctp, ctpI, cpQM, cpQ3, cpt, cptb, cptbI, ctW, ctWI, ctZ, ctZI, cbW, cbWI, ctG, ctGI | [1M ttgamma events](https://cmsweb.cern.ch/das/request?input=%2Fttgamma0j_rwgt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball%2Fllechner-ttgamma0j_order2_15weights_18052018-10fcfa1a1c01204983ea66975abf2caf%2FUSER&instance=prod%2Fphys03)  |
  
##### Reference Point (directory 18052018_ref)
Reference Point: ctW = 4., ctWI = 4., ctZ = 4., ctZI = 4., ctG = 4., ctGI = 4.  
  
| process  | poly order | # coeff | Wilson coefficients                                                                 | Link to gen. events |
|:--------:|:----------:|:-------:|:-----------------------------------------------------------------------------------:|:------------------------:|
| ttZ      | 2          | 15      | ctp, ctpI, cpQM, cpQ3, cpt, cptb, cptbI, ctW, ctWI, ctZ, ctZI, cbW, cbWI, ctG, ctGI | [1M ttZ events](https://cmsweb.cern.ch/das/request?input=%2FttZ0j_rwgt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball%2Fllechner-ttZ0j_order2_15weights_18052018_ref-7a5fde3f5bf89006ee3acec926ca87d8%2FUSER&instance=prod%2Fphys03)  |
| ttW      | 2          | 15      | ctp, ctpI, cpQM, cpQ3, cpt, cptb, cptbI, ctW, ctWI, ctZ, ctZI, cbW, cbWI, ctG, ctGI | [1M ttW events](https://cmsweb.cern.ch/das/request?input=%2FttW0j_rwgt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball%2Fllechner-ttW0j_order2_15weights_18052018_ref-593ea75549b4c51667dffc93040bbda1%2FUSER&instance=prod%2Fphys03)  |
| ttgamma  | 2          | 15      | ctp, ctpI, cpQM, cpQ3, cpt, cptb, cptbI, ctW, ctWI, ctZ, ctZI, cbW, cbWI, ctG, ctGI | [1M ttgamma events](https://cmsweb.cern.ch/das/request?input=%2Fttgamma0j_rwgt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball%2Fllechner-ttgamma0j_order2_15weights_18052018_ref-10fcfa1a1c01204983ea66975abf2caf%2FUSER&instance=prod%2Fphys03)  |

  
  
### 07/05/2018  
| process  | poly order | # coeff | Wilson coefficients                        | Link to gen. events   |
|:--------:|:----------:|:-------:|:------------------------------------------:|:---------------------:|
| ttZ      | 2          | 8       | cpQM, cpt, ctW, ctWI, ctZ, ctZI, ctG, ctGI | not (yet) processed!  |
| ttW      | 2          | 8       | cpQM, cpt, ctW, ctWI, ctZ, ctZI, ctG, ctGI | not (yet) processed!  |
| ttgamma  | 2          | 8       | cpQM, cpt, ctW, ctWI, ctZ, ctZI, ctG, ctGI | not (yet) processed!  |
  
| process  | poly order | # coeff | Wilson coefficients                        | Link to gen. events |
|:--------:|:----------:|:-------:|:------------------------------------------:|:-------------------:|
| ttZ      | 3          | 8       | cpQM, cpt, ctW, ctWI, ctZ, ctZI, ctG, ctGI | [1M ttZ events](https://cmsweb.cern.ch/das/request?input=%2FttZ0j_rwgt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball%2Fllechner-ttZ0j_order3_8weights-7a5fde3f5bf89006ee3acec926ca87d8%2FUSER&instance=prod%2Fphys03) |
| ttW      | 3          | 8       | cpQM, cpt, ctW, ctWI, ctZ, ctZI, ctG, ctGI | [1M ttW events](https://cmsweb.cern.ch/das/request?input=%2FttW0j_rwgt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball%2Fllechner-ttW0j_order3_8weights-593ea75549b4c51667dffc93040bbda1%2FUSER&instance=prod%2Fphys03) |
| ttgamma  | 3          | 8       | cpQM, cpt, ctW, ctWI, ctZ, ctZI, ctG, ctGI | [1M ttgamma events](https://cmsweb.cern.ch/das/request?input=%2Fttgamma0j_rwgt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball%2Fllechner-ttgamma0j_order3_8weights-10fcfa1a1c01204983ea66975abf2caf%2FUSER&instance=prod%2Fphys03) |  
  
### 03/05/2018  
##### Error in the pdfHandler!  

| process  | poly order | # coeff | Wilson coefficients                        | Link to gen. events   |
|:--------:|:----------:|:-------:|:------------------------------------------:|:---------------------:|
| ttZ      | 2          | 8       | cpQM, cpt, ctW, ctWI, ctZ, ctZI, ctG, ctGI | not (yet) processed!  |
| ttW      | 2          | 8       | cpQM, cpt, ctW, ctWI, ctZ, ctZI, ctG, ctGI | not (yet) processed!  |
| ttgamma  | 2          | 8       | cpQM, cpt, ctW, ctWI, ctZ, ctZI, ctG, ctGI | not (yet) processed!  |
  
| process  | poly order | # coeff | Wilson coefficients                        | Link to gen. events   |
|:--------:|:----------:|:-------:|:------------------------------------------:|:---------------------:|
| ttZ      | 3          | 8       | cpQM, cpt, ctW, ctWI, ctZ, ctZI, ctG, ctGI | not (yet) processed!  |
| ttW      | 3          | 8       | cpQM, cpt, ctW, ctWI, ctZ, ctZI, ctG, ctGI | not (yet) processed!  |
| ttgamma  | 3          | 8       | cpQM, cpt, ctW, ctWI, ctZ, ctZI, ctG, ctGI | not (yet) processed!  |
  
