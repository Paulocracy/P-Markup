#!/usr/bin/env python
# Copyright 2018 Paulocracy
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import tkinter
import tkinter.filedialog


class DirectorySelection:
    def __init__(self, frame, text, directory="N/A"):
        """Initializes a combined label/directory selection widget"""
        self.frame = tkinter.Frame(frame)
        self.text = text
        self.directory = directory
        
        self.label = tkinter.Label(self.frame, text=self.text+self.directory)
        self.button = tkinter.Button(self.frame, text="Select...", command=self._select_directory)
    
    def _select_directory(self, *events):
        """Sets the filepath according to the user's selection."""
        directory = tkinter.filedialog.askdirectory()
        if directory:
            self.directory = directory
            self.label["text"] = self.text+self.directory
    
    def get(self):
        """Returns the selected directory."""
        return self.directory
    
    def pack(self):
        """Packs the combined widget."""
        self.frame.pack(expand=True, fill="y")
        self.label.pack(side="left")
        self.button.pack(side="left")
