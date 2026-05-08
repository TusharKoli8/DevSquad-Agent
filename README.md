# Multi Agent QA Engineering System

An intelligent agent based software engineering workflow where multiple AI agents collaborate to develop, review, test, fix, and validate code before final delivery.

This project mimics a real engineering pipeline used in software teams by combining autonomous agents with graph based decision routing.

## Features

- Requirement-to-code generation  
- Automated code review and best practice validation  
- Edge case testing and QA verification  
- Bug fixing and code optimization  
- Conditional routing based on quality checks  
- Final engineering report generation  


## Real Engineering Workflow

User Requirements  
↓  

Developer Agent  
↓  

Review Agent  
↓  

QA Agent  
↓  

Decision Routing  

If issues found → Fix Agent → Review Again  

If passed → Final Report → END  


## Architecture


User Requirements

        |
        
        V
        
Developer Agent

        |
        
        V
        
Review Agent

        |
        
        V
        
QA Agent
        |
        
        V
        
 Routing Logic
 
   /        \
   
  V          V
  
Fix Agent   Final Report

  |
  
  V
  
Review Agent

  |
  
 END

## Run

---bash 

## Create env

uv venv

--activate it

uv pip install -r requirements.txt

---bash

python main.py
