## @package Kniffel.Info
# @brief module that contains all information about the tool Kniffel.
# @details module that contains all information about Kniffel.


import os, time

## @brief Kniffel version
# @details Kniffel version
# Get the version from the version.py file
with open('version.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.split('=')[-1].strip().strip('"')
            break

## @brief Kniffel xml config version
# @details Kniffel xml config version
config_version = '0.0.1'

## @brief Kniffel Logging File head
# @details Kniffel Logging File head
logginghead = """====================================================================
  Kniffel
  Version %s                           
  Logging File                           
                                                
====================================================================
"""
