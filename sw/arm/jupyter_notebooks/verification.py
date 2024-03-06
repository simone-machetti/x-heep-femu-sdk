# Copyright 2023 EPFL
# Solderpad Hardware License, Version 2.1, see LICENSE.md for details.
# SPDX-License-Identifier: Apache-2.0 WITH SHL-2.1
#
# Author: Deniz Kasap - deniz.kasap@epfl.ch

import os
import subprocess
import datetime
import time

list_of_tests = [file for file in os.listdir(os.getcwd()) if file.endswith('.ipynb')]
print(f"{len(list_of_tests)} applications to be tested.")

for file in list_of_tests:
    print(f"Launched {file[:-6].ljust(max(len(s)-6 for s in list_of_tests))} at {datetime.datetime.now().strftime('%H:%M:%S')}", end=' ', flush=True)
    (out, err) = subprocess.Popen( f"ipython -c \"%run {file}\"", stdout=subprocess.PIPE, shell=True).communicate()
    print("✅" if "Test Passed!" in out.decode() else "❌" )