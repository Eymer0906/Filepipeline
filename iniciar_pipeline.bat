@echo off
chcp 65001 >nul
title FilePipeline - Monitoreo de Archivos
cd /d C:\FilePipeline
echo ========================================
echo  FilePipeline - Iniciando monitoreo
echo ========================================
pythonw pipeline.py
