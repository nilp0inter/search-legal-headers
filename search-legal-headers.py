#!/usr/bin/env python
"""
Copyright 2020 Roberto Abdelkader Martínez Pérez

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""

import json
import sys
from glob import glob

all_good = True

with open('.licenserc.json') as cfgfile:
    config = json.load(cfgfile)
    for expr, needle in config.items():
        for filename in glob(expr, recursive=True):
            with open(filename, 'r') as haystack:
                if needle not in haystack.read():
                    print(filename + ": missing legal header '" + needle[:20].replace('\n', ' ') + "'...")
                    all_good = False

if not all_good: sys.exit(1)
