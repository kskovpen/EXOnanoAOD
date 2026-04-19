#!/bin/env python3

import os, sys

output = "driver"

for run in ["run3_2022_mc", "run3_2022EE_mc", "run3_2023_mc", "run3_2023BPix_mc", "run3_2024_mc", "run3_2022", "run3_2023", "run3_2024"]:

    if run == "run3_2022_mc":
        
        os.system("cmsDriver.py step3 \
        --mc \
        --conditions 150X_mcRun3_2022_realistic_v1 \
        --datatier NANOAODSIM \
        --era Run3,run3_nanoAOD_pre142X \
        --eventcontent NANOAODSIM \
        --filein \"file:step2.root\" \
        --fileout \"file:step3.root\" \
        --nStreams 1 --nThreads 4 \
        --no_exec --number 10 \
        --python_filename "+output+"/step_3_cfg_"+run+".py \
        --step NANO")
        
    elif run == "run3_2022EE_mc":
        
        os.system("cmsDriver.py step3 \
        --mc \
        --conditions 150X_mcRun3_2022_realistic_postEE_v1 \
        --datatier NANOAODSIM \
        --era Run3,run3_nanoAOD_pre142X \
        --eventcontent NANOAODSIM \
        --filein \"file:step2.root\" \
        --fileout \"file:step3.root\" \
        --nStreams 1 --nThreads 4 \
        --no_exec --number 10 \
        --python_filename "+output+"/step_3_cfg_"+run+".py \
        --step NANO")
        
    elif run == "run3_2023_mc":
        
        os.system("cmsDriver.py step3 \
        --mc \
        --conditions 150X_mcRun3_2023_realistic_v1 \
        --datatier NANOAODSIM \
        --era Run3_2023,run3_nanoAOD_pre142X \
        --eventcontent NANOAODSIM \
        --filein \"file:step2.root\" \
        --fileout \"file:step3.root\" \
        --nStreams 1 --nThreads 4 \
        --no_exec --number 10 \
        --python_filename "+output+"/step_3_cfg_"+run+".py \
        --step NANO")
        
    elif run == "run3_2023BPix_mc":
        
        os.system("cmsDriver.py step3 \
        --mc \
        --conditions 150X_mcRun3_2023_realistic_postBPix_v1 \
        --datatier NANOAODSIM \
        --era Run3_2023,run3_nanoAOD_pre142X \
        --eventcontent NANOAODSIM \
        --filein \"file:step2.root\" \
        --fileout \"file:step3.root\" \
        --nStreams 1 --nThreads 4 \
        --no_exec --number 10 \
        --python_filename "+output+"/step_3_cfg_"+run+".py \
        --step NANO")
        
    elif run == "run3_2024_mc":
        
        os.system("cmsDriver.py step3 \
        --mc \
        --conditions 150X_mcRun3_2024_realistic_v1 \
        --datatier NANOAODSIM \
        --era Run3_2024,run3_nanoAOD_pre142X \
        --eventcontent NANOAODSIM \
        --filein \"file:step2.root\" \
        --fileout \"file:step3.root\" \
        --nStreams 1 --nThreads 4 \
        --no_exec --number 10 \
        --python_filename "+output+"/step_3_cfg_"+run+".py \
        --step NANO")

    elif run == "run3_2022":
        
        os.system("cmsDriver.py step3 \
        --data \
        --conditions 150X_dataRun3_v5 \
        --datatier NANOAOD \
        --era Run3,run3_nanoAOD_pre142X \
        --eventcontent NANOAOD \
        --filein \"file:step2.root\" \
        --fileout \"file:step3.root\" \
        --nStreams 1 --nThreads 4 \
        --scenario pp \
        --no_exec --number 10 \
        --python_filename "+output+"/step_3_cfg_"+run+".py \
        --step NANO")

    elif run == "run3_2023":
        
        os.system("cmsDriver.py step3 \
        --data \
        --conditions 150X_dataRun3_v5 \
        --datatier NANOAOD \
        --era Run3_2023,run3_nanoAOD_pre142X \
        --eventcontent NANOAOD \
        --filein \"file:step2.root\" \
        --fileout \"file:step3.root\" \
        --nStreams 1 --nThreads 4 \
        --scenario pp \
        --no_exec --number 10 \
        --python_filename "+output+"/step_3_cfg_"+run+".py \
        --step NANO")
        
    elif run == "run3_2024":
        
        os.system("cmsDriver.py step3 \
        --data \
        --conditions 150X_dataRun3_v2 \
        --datatier NANOAOD \
        --era Run3_2024 \
        --eventcontent NANOAOD \
        --filein \"file:step2.root\" \
        --fileout \"file:step3.root\" \
        --nStreams 1 --nThreads 4 \
        --scenario pp \
        --no_exec --number 10 \
        --python_filename "+output+"/step_3_cfg_"+run+".py \
        --step NANO")
        
