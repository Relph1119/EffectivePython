#!/usr/bin/env python3

# Copyright 2014 Brett Slatkin, Pearson Education Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Preamble to mimick book environment
import logging
from pprint import pprint
from sys import stdout as STDOUT


# Example 11
# Reenabling this will break things.
# import app

class Dialog(object):
    def __init__(self):
        pass

# Using this instead will break things
# save_dialog = Dialog(app.prefs.get('save_dir'))
save_dialog = Dialog()

def show():
    import ch07.item_52.recursive_import_dynamic.app as app # Dynamic import
    save_dialog.save_dir = app.prefs.get('save_dir')
    print('Showing the dialog!')
