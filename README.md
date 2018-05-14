Pancreas analysis tool
=====

The close parallel between disease incidence and mortality highlights the poor prognosis associated with pancreatic cancer `1` \cite{siegel2014cancer}. The prevalence was 2098 in 2017 and 5-year survival in the Netherlands remains as low as 9\% in patients with pancreatic cancer `2` \cite{nlKankerregistratie}. Worldwide the incidence ranges from 1 to 10 cases per 100,000 people for all types of pancreatic cancer, 85\% of which are adenocarcinomas `3` \cite{ryan2014pancreatic}. The late stage at which patients are diagnosed is perhaps the most important factor underlying the low survival rate. Development of the disease is often asymptomatic until development into an advanced stage, of which 20\% is feasible for initial resection `4` \cite{gillen2010preoperative}. Potentially curative resection often leads to recurrence `5` \cite{siegel2014cancer}. Poor chemo- and radiotherapy response, early recurrence and metastasis is supported by the tumor biology of pancreatic cancer. Distant metastases complicate 90\% of pancreatic cancer cases according to autopsy series `6` \cite{kamisawa1995hematogenous}. Family history of pancreatic cancer `7` \cite{hruban2010update}, a personal history of smoking `8` \cite{iodice2008tobacco}, chronic pancreatitis `9` \cite{raimondi2010pancreatic} and diabetes mellitus `10,11` \cite{bosetti2014diabetes,sah2013new} have been identified as risk factors for pancreatic cancer.

Deep learning
-----

The popularity of machine learning in medical imaging has grown in the past years, mostly due to hardware improvements, allowing for faster training of a convolutional neural network (CNN). But also due to data availability. 
Employing CNNs in the processing of volumetric data has taken a lot of effort, 2D CNNs have been used to aggregate 3D features in adjacent slices `12` \cite{chen2015automatic}, multi-view planes `13` \cite{setio2016pulmonary} or orthogonal planes `14` \cite{prasoon2013deep}. However, none of these methods make full use of the 3D spatial information effectively `15` \cite{yu2017volumetric}. Thus, multiple studies started employing 3D CNNs to cope `16, 17` \cite{cciccek20163d,merkow2016dense} with segmentation problems in medical volumetric data based on the design principles of U-Net `18` \cite{ronneberger2015u}.

Goal
-----

The file [hello.py](https://github.com/BartTh/pancreasread/blob/master/hello.py) is a Flask based web application that brings the potential benefit of deep learning to the clinic. This web application has a basic uploading interface, a processing page and an image review page. 

# Manual

The following files are presented:
- [hello.py](https://github.com/BartTh/pancreasread/blob/master/hello.py) &mdash; Main file processing and managing data
- [user_readme](https://github.com/BartTh/pancreasread/blob/master/User_readme.md) &mdash; How to use this tool as a clinician
- [developer_readme](https://github.com/BartTh/pancreasread/blob/master/Developer_readme.md) &mdash; How to use set up a VM to run this application on the google cloud platform
